import os
import sublime
import sublime_plugin

class CreateNewPuppetBase(sublime_plugin.WindowCommand):

    def doCommand(self, dirs):
        # self.window.show_quick_panel(dirs, self.on_selection);
        self.dirs = dirs
        self.window.show_input_panel("Puppet name:", "", self.on_done, None, self.on_cancel);

    def create_puppet(self, puppet_name):
        for dir in self.dirs:
            puppet_path = dir + "/" + puppet_name
            self.create_folder(puppet_path);

            for file in self.file_templates:
                print("created file: " + puppet_path + "/" + puppet_name + file)
                self.create_file(puppet_path + "/" + puppet_name + file);

    def set_file_templates(self, list):
        self.file_templates = list

    def on_done(self, puppet_name):
        self.create_puppet(puppet_name)

        self.window.active_view().set_status("", "[Puppetmaster] === Created new puppet: " + puppet_name + " ===")
        self.window.open_file(self.dirs[0] + "/" + puppet_name + "/" + puppet_name + "_module.js")

    def on_cancel(self):
        self.dirs = None
        self.file_templates = None

        self.window.active_view().set_status("", "[Puppetmaster] === Canceled puppet creation ===")

    def create_file(self, filename):
        try:
            f = open(filename, "w")
        except IOError:
            pass

    def create_folder(self, base):
        if not os.path.exists(base):
            parent = os.path.split(base)[0]
            if not os.path.exists(parent):
                self.create_folder(parent)
            os.mkdir(base)


class CreateNewPuppet(CreateNewPuppetBase):

    def run(self, dirs = []):
        if len(dirs) == 0:
            self.window.active_view().set_status("", "[Puppetmaster] === Select a folder for this command! ===")
            return

        file_templates = [ "_module.js", "_view.js" ]
        self.set_file_templates(file_templates)

        self.doCommand(dirs)
