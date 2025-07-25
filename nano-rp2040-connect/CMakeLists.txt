# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)
set(PICO_SDK_PATH "${PICO_SDK_PATH}" )

set(PICO_BOARD arduino_nano_rp2040_connect CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

if (PICO_SDK_VERSION_STRING VERSION_LESS "1.4.0")
  message(FATAL_ERROR "Raspberry Pi Pico SDK version 1.4.0 (or later) required. Your version is ${PICO_SDK_VERSION_STRING}")
endif()

project(nano-rp2040-connect C CXX ASM)

set(PICO_CXX_ENABLE_EXCEPTIONS 1)

set(PICO_CXX_ENABLE_RTTI 1)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(nano-rp2040-connect nano-rp2040-connect.cpp )

pico_set_program_name(nano-rp2040-connect "nano-rp2040-connect")
pico_set_program_version(nano-rp2040-connect "0.1")

# no_flash means the target is to run from RAM
pico_set_binary_type(nano-rp2040-connect no_flash)

pico_enable_stdio_uart(nano-rp2040-connect 1)
pico_enable_stdio_usb(nano-rp2040-connect 1)

# Add the standard library to the build
target_link_libraries(nano-rp2040-connect
        pico_stdlib)

# Add the standard include files to the build
target_include_directories(nano-rp2040-connect PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}
  ${CMAKE_CURRENT_LIST_DIR}/.. # for our common lwipopts or any other standard includes, if required
)

# Add any user requested libraries
target_link_libraries(nano-rp2040-connect 
        hardware_spi
        hardware_i2c
        hardware_dma
        hardware_pio
        hardware_interp
        hardware_timer
        hardware_watchdog
        hardware_clocks
        )

pico_add_extra_outputs(nano-rp2040-connect)

