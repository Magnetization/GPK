# GPK (Gliding on Physical Keyboard)

We introduce a novel typing technique for special symbols in the keyboard-only environment.
With the technique, called GPK (Gliding on Physical Keyboard), users can literally draw on the keyboard to enter special symbols.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites and Installing

What things you need to install and how to install them

```
git clone https://github.com/Magnetization/GPK-CHISRC
cd GPK-CHISRC
pip install fastdtw, keyboard==0.11.0
python main.py
```
note: GPK may not work well on Linux or Mac OS due to [keyboard](https://github.com/boppreh/keyboard)

## usage
As GPK will not influence your normal typing, you cam simply glide on the keyboard whenever and wherever you want to. The recognition precedure will be triggred automatically. For example <br>
![alpha](/imgs/demo_alpha.gif)
<br>
Here you can press number keys 1-5 to select from the symbols. If what you want is not in the list, you can press '`', which is the left key of number key '1', to cancel

## Built With

* [keyboard](https://github.com/boppreh/keyboard) - keyboard hook used
* [fastDTW](https://github.com/slaypni/fastdtw) - Used to recognize symbols


## Authors

* **Xiyuan He** - *Initial work* - [Magnetization](https://github.com/Magnetization)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
