# Evaluating QUIC Performance over Web, Cloud Storage and Video Workloads

[Tanya Shreedhar](https://www.iiitd.edu.in/~tanyas/) (IIIT-Delhi) | Rohit Panda (TUM) | Sergey Podanev (TUM) | Vaibhav Bajpai (TUM)


If you use our dataset and scripts for your research, please cite our [Publication](https://doi.org/10.1109/INFOCOM41043.2020.9155367).

> T. Shreedhar, R. Panda, S. Podanev and V. Bajpai, "Evaluating QUIC Performance over Web, Cloud Storage and Video Workloads," in IEEE Transactions on Network and Service Management, doi: 10.1109/TNSM.2021.3134562.


---

### Dataset

Coming Soon

### Tests

Coming Soon

### Analysis Reproducibility

You can access our analysis scripts from the `analysis-scripts` folder.

#### Requirements
The analyses were performed using `jupyter` notebooks on `Python 3`.
Required Python dependencies are listed as follows.

        Package          Version
        ipython          6.1.0
        matplotlib       2.1.0
        numpy            1.13.3
        pandas           00.3
        requests         2.18.4

For the calculation of CDFs and drawing of the corresponding plots, `Pmf.py` &rarr; and `Cdf.py` &rarr; from [Think Stats &rarr;](https://greenteapress.com/wp/think-stats-2e/) are used.

#### Description


-  `CPU Utilisation-Gdrive.ipynb` &rarr; CPU utilization downloading from Gdrive with `quic\_perf` and `tls\_perf`
-  `CPU Utilisation-Youtube.ipynb` &rarr; CPU utilization with YouTube tests
-  `Gdrive CPU Utilisation- Throughput.ipynb` &rarr; Scatter Plots with quic\_perf and tls\_perf
-  `Gdrive - Throughput.ipynb` &rarr; Throughput downloading from Gdrive with quic\_perf and tls\_perf
-  `IETF QUIC.ipynb` &rarr; Connection Time, TTFB, Download Time at VM for IETF QUIC
-  `Master-Thesis-Gdrive-PI.ipynb` &rarr; Connection Time, TTFB, Download Time at Munich for downloading from Gdrive
-  `Master-Thesis-India.ipynb` &rarr; Connection Time, TTFB, Download Time at India
-   `Master-Thesis.ipynb` &rarr; Connection Time, TTFB, Download Time at VM
-   `Master-Thesis-PI-Munich.ipynb` &rarr; Connection Time, TTFB, Download Time at Munich
-  `Quic - ASN.ipynb` &rarr; AS Analysis
-  `System Calls.ipynb` &rarr; System calls using strace
-  `Throughput-combined flows.ipynb` &rarr; Throughput with multiple flows downloading from Gdrive with quic\_perf and tls\_perf
-  `Youtube CPU Utilisation- Throughput.ipynb` &rarr; Scatter Plots with YouTube tests
-  `YoutubeThroughput-combined flows.ipynb` &rarr; Throughput with multiple flows with YouTube tests
-  `Youtube - Throughput.ipynb` &rarr; Throughput with YouTube tests


### Contact

Please contact us for further details.

- Tanya Shreedhar (<tanyas@iiitd.ac.in>)(corresponding author)
- Rohit Panda (<rohit.panda21@gmail.com>)
- Sergey Podanev (<sergey.podanev@tum.de>)
- Vaibhav Bajpai (<bajpaiv@in.tum.de>)
