[![IR Candles](https://img.shields.io/github/v/release/astrandb/ir_candles)](https://github.com/astrandb/ir_candles/releases/latest) [![hacs_badge](https://img.shields.io/badge/HACS-Custom-blue.svg)](https://github.com/hacs/integration) ![Validate with hassfest](https://github.com/astrandb/ir_candles/workflows/Validate%20with%20hassfest/badge.svg) ![Maintenance](https://img.shields.io/maintenance/yes/2026.svg) [![IR Candles_downloads](https://img.shields.io/github/downloads/astrandb/ir_candles/latest/total)](https://github.com/astrandb/ir_candles)

# IR Candles - Integration for Home Assistant

This integration exposes LED candles with an IR blaster. It works with all IR emitters (e.g. Broadlink, ESP Home, etc) that are registered in Home Assistant. The codes emitted are reverse engineered from physical remote controls.

Note that the installation supports multiple blasters, but there is a fair chance that different remotes use overlapping code maps that can cause some chaos if you have different brands in one room.

Please also note that as the IR protocol is one-way transmit only, there is no possibility for the integration to know if the candle is on or off. However, best effort is used to keep track of assumed state.

## Installation

### Preferred download method

- Install your IR blaster first.
- Use Marketplace in Home Assistant, add this repo as a custom repository (Add from link button) and install "IR Candles" integration.

### Manual download method

- Copy all files from custom_components/ir_candles in this repo to your config custom_components/ir_candles
- Restart Home Assistant

### Setup

Goto Integrations->Add and select "IR Candles"

Follow instructions to setup the integration.

## Disclaimer

The package and its author are not affiliated with candle manufacturers. Use at your own risk.

## License

The package is released under the MIT license.
