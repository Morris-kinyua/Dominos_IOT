# IoT Device Selector for Multi-Company

A clean Odoo module that adds device selection and validation for multi-company fiscal device operations.

## Features

- **Device Assignment**: Assign IoT devices to specific companies
- **Device Selection Wizard**: When sending to fiscal device, users select from available devices
- **Device Validation**: Prevents sending to wrong device with clear error messages
- **Multi-Company Support**: Enforces company-device mapping constraints

## How It Works

### Setup

1. Navigate to **Settings > IoT > Devices**
2. For each IoT device, set:
   - **Company**: The company this device belongs to
   - **Device Name**: Friendly identifier (e.g., "xyz" for Company A)

3. Navigate to **Settings > Companies & Branches**
4. For each company, set:
   - **Fiscal Device**: Select the assigned IoT device

### Usage

1. Open a company record
2. Click **"Send to Fiscal Device"** button
3. A wizard appears showing available devices for that company
4. Select the correct device and confirm
5. If wrong device is selected, error: "Wrong device selected. Device 'xyz' is not assigned to company 'Company A'"

## Technical Details

### Models

- **iot.device** (inherited)
  - `company_id`: Many2one to res.company
  - `device_name`: Friendly name for identification

- **res.company** (inherited)
  - `iot_device_id`: Many2one to iot.device with domain filter
  - `action_send_to_fiscal_device()`: Opens device selector wizard

- **iot.device.selector** (transient)
  - Device selection wizard with validation
  - Enforces company-device matching

### Validation

- Constraint on `res.company.iot_device_id` ensures device belongs to company
- Wizard validates device selection before proceeding
- Clear error messages for mismatched devices

## Dependencies

- `iot`: Base IoT module
- `l10n_ke_etims_vscu`: Kenyan eTIMS VSCU module

## Installation

1. Place module in `/customs/iot_device_selector/`
2. Update app list
3. Install "IoT Device Selector for Multi-Company"
