# Verilog PCIe AC701 Example Design

## Introduction

This example design targets the Xilinx AC701 FPGA board.

The design implements the PCIe AXI lite master module, the PCIe AXI master module, and the PCIe DMA module.  A very simple Linux driver is included to test the FPGA design.

*  FPGA: xc7a200t-2-fbg676 

## How to build

Run `make` to build.  Ensure that the Xilinx Vivado components are in PATH.

Run `make` to build the driver.  Ensure the headers for the running kernel are installed, otherwise the driver cannot be compiled.

## How to test

Run `make program` to program the AC701 board with Vivado.  Then load the driver with `insmod example.ko`.  Check dmesg for the output.
