from vmcloak.abstract import Dependency

class RemoveTips(Dependency):
    name = "removetips"
    exes = [
        {
            "url": "http://cuckoo.sh/vmcloak/MicrosoftFixit50048.msi",
            "sha1": "0de68031b1c1d17bf6851b13f2d083ee61b6b533",
        },
    ]

    def run(self):
	      self.upload_dependency("C:\\MicrosoftFixit50048.msi")
        self.a.execute("msiexec /i C:\\MicrosoftFixit50048.msi /passive /norestart")
        self.a.remove("C:\\MicrosoftFixit50048.msi")