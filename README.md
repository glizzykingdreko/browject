# BrowJect

![BrowJect Logo](img/banner.png)

BrowJect is a cutting-edge Python library designed to provide direct access to browser attributes, bridging the gap between browser interactions and Python. This tool is invaluable for reverse engineering antibots, allowing you to monitor and use browser attributes directly in Python. With BrowJect, you can emulate browser behaviors with precision and ease.

## Table of Contents
- [BrowJect](#browject)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Use Case: Reverse Engineering Antibots](#use-case-reverse-engineering-antibots)
  - [Special Thanks](#special-thanks)

## Features

- **Dynamic Browser Loading:** Load any Chrome browser based on user agent, version, or operating system. This allows for unmatched flexibility and precision in your interactions.
  
- **Up-to-date Browser Database:** Thanks to [TakionAPI](https://takionapi.tech/), BrowJect's database is always updated with any Chrome version, model, or OS. TakionAPI is the premier provider of antibot bypass APIs.

- **Easy to Use:** BrowJect provides a simple interface to fetch and work with browser attributes.

- **Ideal for Reverse Engineering:** Aid your reverse engineering efforts against antibots by directly accessing browser attributes in Python.

## Installation

Install BrowJect using pip:

```bash
pip install browject
```

## Usage

After installing, you can easily create a browser object based on user agent, version, or operating system, and then access its attributes:

```python
from browject import BrowJect

browser = BrowJect(chrome_version='112', operating_system='macOS')
print(browser.navigator.userAgent)

browser2 = BrowJect(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
print(browser2.navigator.userAgent)
```

### Use Case: Reverse Engineering Antibots

When working on antibots, it's crucial to understand and replicate the exact behaviors and attributes of a browser. With BrowJect, this task becomes seamless. For instance, if an antibot checks for specific plugins or screen dimensions, you can access and use these attributes directly in Python:

```python
# Accessing browser plugins 
plugins = browser.navigator.plugins

# Checking screen dimensions 
screen_width = browser.screen.width
screen_height = browser.screen.height
```

This direct access significantly eases the process of replicating browser behaviors and aids in bypassing antibots.

## Special Thanks

A special shoutout to [TakionAPI](https://takionapi.tech/) - the best antibot bypass APIs provider. If you haven't tried them yet, you're missing out. Join their [Discord](https://takionapi.tech/discord) for a free trial!

Additionally, a massive thank you to the developer behind BrowJect, **glizzykingdreko**. You can find him on [Medium](https://medium.com/@glizzykingdreko), [GitHub](https://github.com/glizzykingdreko), and [Twitter](https://twitter.com/glizzykingdreko). For any inquiries, reach out via email: glizzykingdreko@protonmail.com.