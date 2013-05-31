import sublime, sublime_plugin

class ToggleImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        import_statements = view.find_all(r'^import')

        if len(import_statements) > 0:
            start = view.line(import_statements[0]).begin() + 7
            end = view.line(import_statements[-1]).end()

            if not view.fold(sublime.Region(start, end)):
                view.unfold(sublime.Region(start, end))