<h1 align="center">Welcome to gb-menu 👋</h1>
<p>
  <a href=https://pypi.org/project/gb-menu" target="_blank">
    <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/gb-menu">
  </a>
  <a href=https://github.com/gbeard2/gb-menu target="_blank">
    <img alt="Release" src="https://img.shields.io/github/v/release/gbeard2/gb-menu">
  </a>
  <a href=https://pypi.org/project/gb-menu" target="_blank">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/gb-menu">
  </a>
  <a href="https://github.com/gbeard2/gb-menu/commits" target="_blank">
    <img alt="Weekly Commits" src="https://img.shields.io/github/commit-activity/w/gbeard2/gb-menu" />
  </a>
</p>

> A lightweight Python library useful for creating powerful yet simple console-based user interfaces

## Install

```sh
pip install gb-menu
```

## Usage

```python
from gb_menu import menu, choice, action

main_menu = menu.Menu()
cont_action = action.Action(function=type(None))
cont_choice = choice.Choice(key='c', text='Continue', action=cont_action)
main_menu.add_choice(cont_choice)
quit_action = action.Action(function=exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action)
main_menu.add_choice(quit_choice)

while True:
    main_menu.show()
```

## Output

```sh
c: Continue
q: Quit
Choice: c
c: Continue
q: Quit
Choice: c
c: Continue
q: Quit
Choice: q

Process finished with exit code 0
```

## Author

👤 **Garrett Beard**

* Github: [@gbeard2](https://github.com/gbeard2)
* LinkedIn: [@garrett-beard](https://linkedin.com/in/garrett-beard)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/gbeard2/gb-menu/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Garrett Beard](https://github.com/gbeard2). <br/>
This project is [MIT](https://github.com/gbeard2/gb-menu/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_