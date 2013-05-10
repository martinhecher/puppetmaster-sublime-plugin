puppetmaster-sublime-plugin
===========================

A Sublime Text 2 plugin for working with the 'puppetmaster' toolchain. The suggested workflow is heavily influenced by Brian Mann's backbonetrails tutorials (which I highly recommend for building structured web applications, see http://www.backbonerails.com/). Puppetmaster is based on MarionetteJS (http://marionettejs.com), a great building block library for client side web development.

The plugin supports you with a  workflow for creating so called 'Puppets', which are elements within a web application. The goal of the plugin is to further reduce boilerplate code when building applications.

## Installation

At the moment there is not installable package for sublime. To install the plugin simply clone the repository within the Sublime Text 'Packages' folder like so:

git clone git@github.com:martinhecher/puppetmaster-sublime-plugin.git Puppetmaster

Afterwards the functionality is available within the editor. See 'Usage' on how to use the plugin.

## Usage

### Sidebar enhancements

With a right-click on a folder in the Sidebar the new entry "New Puppet..." is available to create a file/folder structure for a Puppet.

### Snippets

The plugin provides snippets for the different parts of puppetmaster with a reasonable setup. The snippets live within the 'pm-' namespace (for puppetmaster). Currently they are:

* pm-controller
* pm-module
* pm-itemview
* pm-collectionview
* pm-compositeview

Type in the snippet name and press Tab to extract the template code.

