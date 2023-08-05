# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbus_fast', 'dbus_fast._private', 'dbus_fast.aio', 'dbus_fast.glib']

package_data = \
{'': ['*']}

install_requires = \
['async-timeout>=3.0.0']

extras_require = \
{'docs': ['sphinxcontrib-asyncio>=0.3.0,<0.4.0',
          'sphinxcontrib-fulltoc>=1.2.0,<2.0.0',
          'Sphinx>=5.1.1,<6.0.0',
          'myst-parser>=0.18.0,<0.19.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'dbus-fast',
    'version': '1.36.0',
    'description': 'A faster version of dbus-next',
    'long_description': '# dbus-fast\n\n<p align="center">\n  <a href="https://github.com/bluetooth-devices/dbus-fast/actions?query=workflow%3ACI">\n    <img src="https://img.shields.io/github/workflow/status/bluetooth-devices/dbus-fast/CI/main?label=CI&logo=github&style=flat-square" alt="CI Status" >\n  </a>\n  <a href="https://dbus-fast.readthedocs.io">\n    <img src="https://img.shields.io/readthedocs/dbus-fast.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">\n  </a>\n  <a href="https://codecov.io/gh/bluetooth-devices/dbus-fast">\n    <img src="https://img.shields.io/codecov/c/github/bluetooth-devices/dbus-fast.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/dbus-fast/">\n    <img src="https://img.shields.io/pypi/v/dbus-fast.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/dbus-fast.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/dbus-fast.svg?style=flat-square" alt="License">\n</p>\n\nA faster version of dbus-next originally from the [great DBus next library](https://github.com/altdesktop/python-dbus-next) ❤️\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install dbus-fast`\n\n[Documentation](https://dbus-fast.readthedocs.io/en/latest/)\n\ndbus-fast is a Python library for DBus that aims to be a performant fully featured high level library primarily geared towards integration of applications into Linux desktop and mobile environments.\n\nDesktop application developers can use this library for integrating their applications into desktop environments by implementing common DBus standard interfaces or creating custom plugin interfaces.\n\nDesktop users can use this library to create their own scripts and utilities to interact with those interfaces for customization of their desktop environment.\n\ndbus-fast plans to improve over other DBus libraries for Python in the following ways:\n\n- Zero dependencies and pure Python 3\n- An optional cython extension is available to speed up (un)marshalling\n- Focus on performance\n- Support for multiple IO backends including asyncio and the GLib main loop.\n- Nonblocking IO suitable for GUI development.\n- Target the latest language features of Python for beautiful services and clients.\n- Complete implementation of the DBus type system without ever guessing types.\n- Integration tests for all features of the library.\n- Completely documented public API.\n\n## Installing\n\nThis library is available on PyPi as [dbus-fast](https://pypi.org/project/dbus-fast/).\n\n```\npip3 install dbus-fast\n```\n\n## The Client Interface\n\nTo use a service on the bus, the library constructs a proxy object you can use to call methods, get and set properties, and listen to signals.\n\nFor more information, see the [overview for the high-level client](https://dbus-fast.readthedocs.io/en/latest/high-level-client/index.html).\n\nThis example connects to a media player and controls it with the [MPRIS](https://specifications.freedesktop.org/mpris-spec/latest/) DBus interface.\n\n```python\nfrom dbus_fast.aio import MessageBus\n\nimport asyncio\n\n\nasync def main():\n    bus = await MessageBus().connect()\n    # the introspection xml would normally be included in your project, but\n    # this is convenient for development\n    introspection = await bus.introspect(\'org.mpris.MediaPlayer2.vlc\', \'/org/mpris/MediaPlayer2\')\n\n    obj = bus.get_proxy_object(\'org.mpris.MediaPlayer2.vlc\', \'/org/mpris/MediaPlayer2\', introspection)\n    player = obj.get_interface(\'org.mpris.MediaPlayer2.Player\')\n    properties = obj.get_interface(\'org.freedesktop.DBus.Properties\')\n\n    # call methods on the interface (this causes the media player to play)\n    await player.call_play()\n\n    volume = await player.get_volume()\n    print(f\'current volume: {volume}, setting to 0.5\')\n\n    await player.set_volume(0.5)\n\n    # listen to signals\n    def on_properties_changed(interface_name, changed_properties, invalidated_properties):\n        for changed, variant in changed_properties.items():\n            print(f\'property changed: {changed} - {variant.value}\')\n\n    properties.on_properties_changed(on_properties_changed)\n\n    await asyncio.Event().wait()\n\nasyncio.run(main())\n```\n\n## The Service Interface\n\nTo define a service on the bus, use the `ServiceInterface` class and decorate class methods to specify DBus methods, properties, and signals with their type signatures.\n\nFor more information, see the [overview for the high-level service](https://python-dbus-fast.readthedocs.io/en/latest/high-level-service/index.html).\n\n```python\nfrom dbus_fast.service import ServiceInterface, method, dbus_property, signal, Variant\nfrom dbus_fast.aio MessageBus\n\nimport asyncio\n\nclass ExampleInterface(ServiceInterface):\n    def __init__(self, name):\n        super().__init__(name)\n        self._string_prop = \'kevin\'\n\n    @method()\n    def Echo(self, what: \'s\') -> \'s\':\n        return what\n\n    @method()\n    def GetVariantDict() -> \'a{sv}\':\n        return {\n            \'foo\': Variant(\'s\', \'bar\'),\n            \'bat\': Variant(\'x\', -55),\n            \'a_list\': Variant(\'as\', [\'hello\', \'world\'])\n        }\n\n    @dbus_property()\n    def string_prop(self) -> \'s\':\n        return self._string_prop\n\n    @string_prop.setter\n    def string_prop_setter(self, val: \'s\'):\n        self._string_prop = val\n\n    @signal()\n    def signal_simple(self) -> \'s\':\n        return \'hello\'\n\nasync def main():\n    bus = await MessageBus().connect()\n    interface = ExampleInterface(\'test.interface\')\n    bus.export(\'/test/path\', interface)\n    # now that we are ready to handle requests, we can request name from D-Bus\n    await bus.request_name(\'test.name\')\n    # wait indefinitely\n    await asyncio.Event().wait()\n\nasyncio.run(main())\n```\n\n## The Low-Level Interface\n\nThe low-level interface works with DBus messages directly.\n\nFor more information, see the [overview for the low-level interface](https://python-dbus-fast.readthedocs.io/en/latest/low-level-interface/index.html).\n\n```python\nfrom dbus_fast.message import Message, MessageType\nfrom dbus_fast.aio import MessageBus\n\nimport asyncio\nimport json\n\n\nasync def main():\n    bus = await MessageBus().connect()\n\n    reply = await bus.call(\n        Message(destination=\'org.freedesktop.DBus\',\n                path=\'/org/freedesktop/DBus\',\n                interface=\'org.freedesktop.DBus\',\n                member=\'ListNames\'))\n\n    if reply.message_type == MessageType.ERROR:\n        raise Exception(reply.body[0])\n\n    print(json.dumps(reply.body[0], indent=2))\n\n\nasyncio.run(main())\n```\n\n## Projects that use python-dbus-fast\n\n- [Bluetooth Adapters](https://github.com/bluetooth-devices/bluetooth-adapters)\n\n## Contributing\n\nContributions are welcome. Development happens on [Github](https://github.com/altdesktop/python-dbus-fast).\n\nBefore you commit, run `pre-commit run --all-files` to run the linter, code formatter, and the test suite.\n\n## Copyright\n\nYou can use this code under an MIT license (see LICENSE).\n\n- © 2019, Tony Crisci\n- © 2022, Bluetooth Devices authors\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- prettier-ignore-start -->\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- markdownlint-disable -->\n<!-- markdownlint-enable -->\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n<!-- prettier-ignore-end -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## Credits\n\nThis package was created with\n[Cookiecutter](https://github.com/audreyr/cookiecutter) and the\n[browniebroke/cookiecutter-pypackage](https://github.com/browniebroke/cookiecutter-pypackage)\nproject template.\n',
    'author': 'Bluetooth Devices Authors',
    'author_email': 'bluetooth@koston.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bluetooth-devices/dbus-fast',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
