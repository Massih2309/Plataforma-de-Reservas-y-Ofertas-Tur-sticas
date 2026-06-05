import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="turismo_app",
    disable_plugins=[SitemapPlugin]   # ← clase, no string
)
