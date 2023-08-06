import asyncio
from typing import Any, Optional, Set, Tuple
from rich.text import Text
from rich.console import RenderableType
from textual.app import App
from textual.widgets import Footer, ScrollView

from nomenklatura.judgement import Judgement
from nomenklatura.loader import Loader
from nomenklatura.resolver import Resolver
from nomenklatura.entity import CE
from nomenklatura.dataset import DS
from nomenklatura.tui.comparison import render_comparison


class DedupeApp(App):
    def __init__(
        self,
        loader: Optional[Loader[DS, CE]] = None,
        resolver: Optional[Resolver[CE]] = None,
        url_base: Optional[str] = None,
        **kwargs: Any
    ):
        super().__init__(**kwargs)
        self.loader = loader
        self.resolver = resolver
        self.latinize = False
        self.url_base = url_base
        self.ignore: Set[Tuple[str, str]] = set()
        self.comp: Optional[RenderableType] = None
        self.left: Optional[CE] = None
        self.right: Optional[CE] = None
        self.score = 0.0

    async def load_candidate(self) -> None:
        if self.loader is None or self.resolver is None:
            return
        self.comp = Text("No candidates.", justify="center")
        self.left = None
        self.right = None
        self.score = 0.0
        for left_id, right_id, score in self.resolver.get_candidates():
            if (left_id, right_id) in self.ignore:
                continue
            if score is None:
                self.ignore.add((left_id, right_id))
                continue
            if not self.resolver.check_candidate(left_id, right_id):
                self.ignore.add((left_id, right_id))
                continue
            self.left = self.loader.get_entity(left_id)
            self.right = self.loader.get_entity(right_id)
            self.score = score
            if self.left is not None and self.right is not None:
                if self.left.schema.can_match(self.right.schema):
                    self.comp = await render_comparison(
                        self.loader,
                        self.left,
                        self.right,
                        score,
                        latinize=self.latinize,
                        url_base=self.url_base,
                    )
                    break
            self.ignore.add((left_id, right_id))
            await asyncio.sleep(0)

    async def on_load(self, event: Any) -> None:
        await self.bind("x", "positive", "Match")
        await self.bind("n", "negative", "No match")
        await self.bind("u", "unsure", "Unsure")
        await self.bind("l", "latinize", "Latinize")
        await self.bind("s", "save", "Save")
        await self.bind("w", "quit", "Save & exit")
        await self.bind("q", "exit", "Exit now")

    async def decide(self, judgement: Judgement) -> None:
        if self.resolver is None:
            return await self.shutdown()  # type: ignore
        if self.left is None or self.right is None:
            await self.load_candidate()
            await self.force_render()
            return
        self.resolver.decide(self.left.id, self.right.id, judgement=judgement)
        await self.load_candidate()
        await self.force_render()

    async def save_resolver(self) -> None:
        if self.resolver is None:
            return await self.shutdown()  # type: ignore
        self.comp = Text("Saving...", justify="center")
        await self.force_render()
        self.resolver.save()
        self.comp = Text("Saved.", justify="center")
        await self.force_render()
        await asyncio.sleep(1)

    async def action_positive(self) -> None:
        await self.decide(Judgement.POSITIVE)

    async def action_negative(self) -> None:
        await self.decide(Judgement.NEGATIVE)

    async def action_unsure(self) -> None:
        await self.decide(Judgement.UNSURE)

    async def action_latinize(self) -> None:
        self.latinize = not self.latinize
        if self.loader is not None and self.left is not None and self.right is not None:
            self.comp = await render_comparison(
                self.loader,
                self.left,
                self.right,
                self.score,
                latinize=self.latinize,
                url_base=self.url_base,
            )
        await self.force_render()

    async def action_save(self) -> None:
        await self.save_resolver()
        await self.load_candidate()
        await self.force_render()

    async def action_quit(self) -> None:
        await self.save_resolver()
        await self.shutdown()  # type: ignore

    async def action_exit(self) -> None:
        await self.shutdown()  # type: ignore

    async def force_render(self) -> None:
        self.scroll.home()
        self.scroll.refresh(layout=True)
        if self.comp is not None:
            await self.scroll.update(self.comp)

    async def on_mount(self) -> None:
        await self.load_candidate()
        self.scroll = ScrollView(self.comp)
        self.footer = Footer()
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.scroll, edge="top")
