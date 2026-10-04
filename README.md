# Blue and Pink Synth Editor on Raspberry Pi 5

A full-featured editor for the Dreadbox Nymphes synthesizer, running on a Raspberry Pi.

2026, Scott Lumsden

# Features

- View and edit all MIDI-controllable Nymphes parameters in a preset, including modulation matrix and chords
- Recall presets via MIDI Program Change and Bank MSB Messages
- Request SYSEX dump of all presets
- Decode and generate Nymphes preset SYSEX messages
  - This allows full floating-point resolution for most parameters, not just 0-127 MIDI CC values
- Save and load preset files
  - These are human-readable txt files
- Convert syx SYSEX preset files to txt preset files
  - This allows you to see their settings, and to choose where or whether to store them in Nymphes' preset slots
- MIDI pass-through from input ports to Nymphes
- MIDI pass-through from Nymphes to output ports


# Nymphes Setup
- Make sure you have Nymphes Firmware Version 2.1 (still the latest version as of Oct 2026)
- Make sure that MIDI CC send/receive is turned ON
- Make sure that MIDI Program Change send/receive is turned ON
- Make sure that you choose the correct MIDI channel on the Settings page in Blue and Pink Synth Editor

*For assistance with Nymphes' menu system: see the [Dreadbox Nymphes Manual](https://www.dreadbox-fx.com/wp-content/uploads/2024/03/Nymphes_Owners-Manual-v2.0.pdf)*


# Raspberry Pi Setup

## Hardware

- Raspberry Pi 5 (8GB RAM, though 4GB or 2GB might be fine)
- [Original 7 inch Raspberry Pi Touch Display connected to the DISP0 DSI Output](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)


## Flash Raspberry Pi OS Onto SD Card

### Run Raspberry Pi Imager (https://www.raspberrypi.com/software/)

#### Device, OS, Storage:

- Choose Raspberry Pi 5
- Choose Raspberry Pi OS (64 Bit) -- Trixie
- Choose SD Card
- Click Next

#### Customisation:

- Hostname: nymphes
- Username: *Enter a username*
- Password: *Enter a password*
- Configure wireless LAN
- Set the locale settings to match where you are
- Enable SSH
	- Select `Use password authentication`
- Do not enable Raspberry Pi Connect

#### Click the `WRITE` button

#### When writing finishes, remove the SD card and insert it into the RPi's SD card slot

## Boot Raspberry Pi and Log In Via SSH
*This assumes that the raspberry pi has successfully connected to your network*
- `ssh <your username>@nymphes.local` 

## Update the Pi
- `sudo apt-get update` 
- `sudo apt-get full-upgrade -y`

## Enable VNC Access
- `sudo raspi-config`
  - Select `Interface Options`
    - Select `VNC`
	  - Choose `Yes`
  - Select `Finish`

- Try connecting to the RPi via VNC to verify that the VNC server is working

## Enable Samba Access for Sharing the Pi's Files on the Network
This is to make it easy to access presets, logs, etc from another computer

- `sudo apt-get install samba samba-common-bin` 
- Edit samba config: `sudo nano /etc/samba/smb.conf` 
	- In the `[homes]` section:
		- Set `browseable = yes` 
		- Set `read only = no`
    - Save and close the file
- Set a Samba password for the user: `sudo smbpasswd -a <your username>` 
	- You will be prompted to enter a password
- Restart Samba: `sudo systemctl restart smbd` 
- You should now be able to find the RPi's samba share on your network


# Install Blue and Pink Synth Editor

## Install Required Packages
Some of these are prerequisites for kivy, which provides a GUI for Blue and Pink Synth Editor

```
sudo apt-get -y install build-essential git make autoconf automake libtool \
pkg-config cmake ninja-build libasound2-dev libpulse-dev libaudio-dev \
libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev \
libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev \
libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev \
libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev \
python3-dev python3-venv xorg wget libxrender-dev lsb-release
```

## Clone nymphes-osc Repository
- `cd ~`
- `git clone https://github.com/jtpack/nymphes-osc.git`


## Clone this Repository (Blue-and-Pink-Synth-Editor-RPi)
- `cd ~`
- `git clone https://github.com/jtpack/Blue-and-Pink-Synth-Editor-RPi.git`


## Create a Python Virtual Environment for the Project
- `cd ~/Blue-and-Pink-Synth-Editor-RPi`
- `python3 -m venv venv`
- `source venv/bin/activate`


## Install nymphes-osc in the virtual environment
- `pip install -e ~/nymphes-osc`


## Install Blue-and-Pink-Synth-Editor in the virtual environment
- `pip install -e .`


## Run Blue-and-Pink-Synth-Editor to make sure it works
*Note: This must be done from the RPi itself, so do it via VNC. Don't ssh in, as there won't be a graphical environment for the app to run in.*
- `python -m blue_and_pink_synth_editor`


## Compile the app into an executable binary
- `pyinstaller BlueAndPinkSynthEditor.spec`


## Run the compiled app to make sure it works
- `dist/BlueAndPinkSynthEditor/BlueAndPinkSynthEditor`


## Move the compiled app to /usr/local/bin
- `sudo mv dist/BlueAndPinkSynthEditor/ /usr/local/bin/`


## Add Entry in Raspberry Pi Main Menu
- `sudo cp BlueAndPinkSynthEditor.desktop /usr/share/applications`


## Make Blue and Pink Synth Editor Run Automatically on Boot

- Create `~/.config/autostart/` directory if it doesn't exist: `mkdir ~/.config/autostart`

- Copy desktop file to autostart directory: `cp BlueAndPinkSynthEditor.desktop ~/.config/autostart`

- Reboot: `sudo reboot`


# How to quit Blue and Pink Synth Editor
- Connect a keyboard and press the Escape Key
- Or VNC into the RPi and press Escape
