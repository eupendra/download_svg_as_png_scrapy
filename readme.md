# Download SVG files as PNG with Scrapy

## Install Dependecies

### macOS
`brew install cairo libffi`
`pip install CairoSVG`

### Windows

- Download the latest [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
- Install [VC++ runtime](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Run `pip install cairosvg`

### Linux

install the cairo, python3-dev and libffi-dev packages (names may vary for your distribution)

## Further Reading
See [details here](https://cairosvg.org/documentation/)
> - on Windows, you’ll have to install Visual C++ compiler for Python and Cairo;
> - on macOS, you’ll have to install cairo and libffi (with Homebrew for example);
> - on Linux, you’ll have to install the cairo, python3-dev and libffi-dev packages (names may vary for your 
distribution).
