# Phomemo label printer project

A Python-based script for printing labels with QR codes and images on three major operating systems: **Linux**, **macOS**, and **Windows**. This tool allows users to specify custom label sizes, generate QR codes, include images, and print directly to a label printer. In this particular project, the used label printer was a PM-241-BT from [Phomemo](https://phomemo.com) like following image shows. This printer was purchased at [Amazon](http://www.amazon.es). If you want to buy a printer to try this project, you can use one of the following links:

  - [Link1](http://www.amazon.es/dp/B0BSBTWQ17/ref=nosim?tag=pmcunhasilva-21)
  - [Link2](http://www.amazon.es/dp/B0BMKTV8ZL/ref=nosim?tag=pmcunhasilva-21)
  - [Link3](http://www.amazon.es/dp/B0BTYFJR36/ref=nosim?tag=pmcunhasilva-21)
  - [Link4](http://www.amazon.es/dp/B0BTYD7H28/ref=nosim?tag=pmcunhasilva-21)
  - [Link5](http://www.amazon.es/dp/B0CCRSJP5S/ref=nosim?tag=pmcunhasilva-21)
  - [Link6](http://www.amazon.es/dp/B0BS8Q3FZQ/ref=nosim?tag=pmcunhasilva-21)

![PM-241-BT](.doc/images/PM-241-BT.png)

---

## Features

- **Cross-Platform Compatibility**: Works on `Linux`, `MacOS`, and `Windows`.
- **Customizable Labels**: Specify label dimensions (e.g., 50mm x 25mm).
- **QR Code Generation**: Dynamically generate and embed QR codes in labels.
- **Images printing**: Convert images to black & white format and add them to labels.
- **Customizable printing script**: Easy to customize python script to easily fit user needs.

---

## Requirements

### General
- Python 3.7 or later.
- `PM-241-BT` printer from [Phomemo](https://phomemo.com) or similar.
- A working printer series driver setup installed for the respective operating system. Please check Phomemo's driver [download](https://eu.phomemo.com/pages/drivers) page.

---

# Environment Setup

- To check for the `Linux/MacOS` setup preparation, please take a closer look on the following [README](.doc/readmes/README_LINUX_MAC.md) file included in this repository.
- To check for the `Windows` setup preparation, please take a closer look on the following [README](.doc/readmes/README_WINDOWS.md) file included in this repository.

These setup guides cover driver installation, printer configuration, label size customization, and Python script execution to print your labels successfully. The following image shows the output label printed by executing one of both `linux_mac_print.py` or `windows_print.py` with labels with `50mm x 25mm` size.

![final_label](.doc/images/final_label.png)

---

## Contribution and Support

Feel free to contribute to this project by submitting issues or pull requests.

## Acknowledgements

Thank contributors, organizations, or resources that supported the project:

- Acknowledge the [ReportLab](https://www.reportlab.com/), [qrcode](https://github.com/lincolnloop/python-qrcode) and [pillow](https://pillow.readthedocs.io/en/stable/) libraries.
- Special acknowledge to [Xelerate.tech](https://www.xelerate.tech/) team by providing all the necessary material and support to accomplish this project.
