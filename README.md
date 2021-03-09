# prassu-kaur

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p style="font-family:verdana"> An NLP based system that uses Transformers( fine-tuned GPT-2 here) to mimic <a href="https://www.littleinfinite.com/20-of-rupi-kaurs-best-poems/" >Rupi Kaur's poetry </a>style <br> </p>

Example: <br>
<img src ="example.png">

### Built With

* [Fastai](https://www.fast.ai/)

<!-- GETTING STARTED -->
## Getting Started

[NOTE: This only works on WSL and Linux as Windows doesnt support "transformer" architecture yet ] <br>

To get a local copy up and running follow these simple steps.

### Prerequisites
```
pip install torch==1.7.1
pip install fastai==2.2.5
pip install transformers==4.0.0
pip install pandas==1.2.0

```
### Installation and Usage

1. Clone the repo
   ```
   git clone https://github.com/Prasanna28Devadiga/prassu-kaur.git
   ```
2. Install the prerequisites
3. Run the following
```
python3 generate.py "your prompt "
```
4. It will generate a poem with your prompt as the first line/ word.
5. Open Poetry.html to view the poem


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Prasanna Devadiga - [@Prasanna280](https://twitter.com/Prasanna280) - prasanna2019@iiitkottayam.ac.in <br>
Aditya Srinivas Menon - [@karynaur](https://twitter.com/MenonSrinivas) - adityasrinivas20bcs8@iiitkottayam.ac.in



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Data](https://github.com/kanhap99/rupikaur/tree/master/rupis)

