from render_engine import Site, Page, Collection, Blog


class MySite(Site):
    SITE_TITLE = "Jay's Elastic Stack Blog"

site = MySite()

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"


@site.register_collection
class Pages(Collection):
    routes = ["", "pages"] # routes will appear at '/page' and '/pages/page'
    content_path = "content/pages" # collections must have their paths assigned
    template = "page.html"


@site.register_collection
class MyBlog(Blog):
    content_path = 'content' # paths are not recursive
    routes = ["", "pages"]
    # template = "blog_post.html" # This isn't created

site.render(strict=True) # build out the tools
