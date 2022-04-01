from jinja2.utils import markupsafe


class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return markupsafe.Markup(f"<script>\ndocument.write(moment(\"{self.timestamp}\").{format});\n</script>")

    def format(self, fmt):
        return self.render(f"format(\"{fmt}\")")

    def calendar(self):
        return self.render("calendar()")

    def from_now(self):
        return self.render("fromNow()")
