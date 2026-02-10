![GitHub license](https://img.shields.io/github/license/torresflo/Favorite-Game-Box.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Favorite-Game-Box.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Favorite-Game-Box.svg)

<p align="center">
  <h1 align="center">Shortcut Me</h3>

  <p align="center">
    A little python script to help you update your readme file with a random video game from a list.
    <br />
    <a href="https://github.com/torresflo/Favorite-Game-Box/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Installation](#installation)
   * [Preparation work](#preparation-work)
   * [Project setup](#project-setup)
* [Example](#example)
* [Contributing](#contributing)
* [License](#license)

---

## Installation

### Preparation work

Add comments to the place where you want to update in your readme file.

You can add a video game with:
   ```markdown
   <!-- favorite-game-box start -->
   <!-- favorite-game-box end -->
   ```

### Project setup

For updating your github profile README, you can follow [update-video-game-box.yml](https://github.com/torresflo/Favorite-Game-Box/blob/master/.github/workflows/update-video-game-box.yml) to create a GitHub Action in your README repository.

A game from the file `data/games.json` will be randomly picked and placed in the readme file each time the workflow is ran. The current list corresponds to my own personal preferences. The best way to customize it to your needs is to fork the project, update the JSON file and replace the repository address in the workflow file (`update-video-game-box.yml`).

## Example

Here is an example from my own profile that you could obtain:

![Example image](https://raw.githubusercontent.com/torresflo/Favorite-Game-Box/main/examples/example1.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the [GNU General Public License v3.0](./LICENSE). See `LICENSE` for more information.