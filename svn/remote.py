from typing import Optional, MutableMapping

import svn.common
import svn.constants


class RemoteClient(svn.common.CommonClient):
    def __init__(
        self,
        url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        svn_filepath: str = "svn",
        trust_cert: Optional[bool] = None,
        env: Optional[MutableMapping[str, str]] = None,
    ) -> None:
        super(RemoteClient, self).__init__(
            url, svn.constants.LT_URL, username, password, svn_filepath, trust_cert, env
        )

    def checkout(self, path: str, revision: Optional[int] = None) -> None:
        cmd = []
        if revision is not None:
            cmd += ["-r", str(revision)]

        cmd += [self.url, path]

        self.run_command("checkout", cmd)

    def remove(self, rel_path: str, message: str, do_force: bool = False) -> None:
        args = [
            "--message",
            message,
        ]

        if do_force is True:
            args.append("--force")

        url = "{}/{}".format(self.url, rel_path)

        args += [url]

        self.run_command("rm", args)

    def __repr__(self) -> str:
        return "<SVN(REMOTE) %s>" % self.url
