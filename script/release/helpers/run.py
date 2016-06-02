#!/usr/bin/env python

import shlex
import subprocess
import collections

class Run:

    @classmethod
    def run(cls, command, **kwargs):
        shell = kwargs.get("shell", False)
        stdin = kwargs.get("stdin", None)
        stdout = kwargs.get("stdout", None)
        stderr = kwargs.get("stderr", None)

        kwargs.update(shell=shell)
        kwargs.update(stdin=stdin)
        kwargs.update(stdout=stdout)
        kwargs.update(stderr=stderr)

        return subprocess.Popen(shlex.split(command), **kwargs)

    @classmethod
    def call(cls, command, **kwargs):
        shell = kwargs.get("shell", False)
        stdin = kwargs.get("stdin", None)
        stdout = kwargs.get("stdout", None)
        stderr = kwargs.get("stderr", None)

        kwargs.update(shell=shell)
        kwargs.update(stdin=stdin)
        kwargs.update(stdout=stdout)
        kwargs.update(stderr=stderr)

        return subprocess.call(shlex.split(command), **kwargs)

    @classmethod
    def observe(cls, command, **kwargs):
        shell = kwargs.get("shell", False)
        stdin = kwargs.get("stdin", subprocess.PIPE)
        stdout = kwargs.get("stdout", subprocess.PIPE)
        stderr = kwargs.get("stderr", subprocess.PIPE)

        kwargs.update(shell=shell)
        kwargs.update(stdin=stdin)
        kwargs.update(stdout=stdout)
        kwargs.update(stderr=stderr)

        proc = subprocess.Popen(shlex.split(command), **kwargs)

        try:
            _stdin = proc.stdin.read()
        except IOError:
            _stdin = None

        try:
            _stdout = proc.stdout.read()
        except IOError:
            _stdout = None

        try:
            _stderr = proc.stderr.read()
        except IOError:
            _stderr = None

        if not _stdin:
            _stdin = None

        if not _stdout:
            _stdout = None

        if not _stderr:
            _stderr = None

        Result = collections.namedtuple("result", "stdin, stdout, stderr")

        return Result(stdin=_stdin, stdout=_stdout, stderr=_stderr)