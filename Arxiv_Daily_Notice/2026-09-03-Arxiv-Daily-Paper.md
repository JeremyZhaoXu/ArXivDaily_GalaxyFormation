# Showing new listings for Thursday, 3 September 2026
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['COLIBRE', 'JWST', 'high redshift', 'descendant']


Excluded: ['interstellar medium', 'standard candle', 'X-ray binar', 'solar corona', 'Instrumentation', 'planet']


### Today: 6papers 
#### Amortized Opacity Marginalization Improves C/O Interval Calibration for Brown-Dwarf Retrievals
 - **Authors:** Kellen Heraty
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Earth and Planetary Astrophysics (astro-ph.EP); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2609.01665

 - **Pdf link:** https://arxiv.org/pdf/2609.01665

 - **Abstract**
 Molecular line lists disagree at a level that measurably shifts retrieved C/O, so retrievals conditioned on a single list omit a dominant systematic from their error bars. Classical marginalization re-runs a full retrieval under K opacity realizations per object. We move that cost into simulation: while generating the training set we randomize opacities (smooth multiplicative Fourier fields in $\log\nu$ plus a discrete line-list mixture, under a deliberately broad prior informed by measured inter-list differences), so a neural posterior estimator learns an already-marginalized posterior. Conceptually, this is the amortized analogue of repeating a conventional retrieval under many plausible opacity realizations and averaging the resulting posteriors. On perturbed held-out spectra (n=2048) a standard NPE covers nominal 90% C/O intervals 43.3% of the time against 82.4% for a compute-matched marginalized network; three-seed control ensembles reach 93.2% on clean data but 61.4% under perturbation, against 89.4% marginalized, isolating the deficit as opacity-induced (TARP joint expected-coverage deviation 0.005 against 0.035). An axis ablation traces the gain to the continuous field (45.4% for the discrete swaps alone, 79.3% for the field alone). Applying the 105 real bad-pixel masks with median filling then collapsed the ensemble's C/O coverage from 0.901 to 0.479; retraining on the same mask distribution and pooling three such seeds returns a nominal 0.905 C/O and 0.891 overall under the full deployment path, still in simulation (n=1024, same 105 masks), at 0.21 to 0.31 of the prior width. On 105 JWST/G395H spectral products of 13 late-T/Y dwarfs, single marginalized networks bracket the Hood et al. (2024) T8 benchmark C/O where the control excludes it, a consistency check rather than a validation, at 1.6-2.6x wider intervals.
#### JWST Reveals a Candidate Supermassive Black Hole Binary at z=4.3 in the Brightest Sub-millimeter Galaxy in COSMOS-Web
 - **Authors:** Jed McKinney, Ansh Gupta, Julian B. Munoz, John Chisholm, Caitlin M. Casey, Stephanie M. Urbano Stawinski, Olivia Cooper, Erini Lambrides, Hollis Akins, Maximilien Franco, Archana Aravindan, Seiji Fujimoto, Kohei Inayoshi, Andreas L. Faisst, Jeyhan S. Kartaltepe, Michael Boylan-Kolchin
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/2609.01711

 - **Pdf link:** https://arxiv.org/pdf/2609.01711

 - **Abstract**
 We present JWST/NIRSpec PRISM and G395M grating spectroscopy for AzTEC-1, a massive sub-mm bright galaxy at $z=4.34$ in the COSMOS extragalactic field. The PRISM spectrum reveals strong H$\alpha$, a significant Balmer break, and no H$\beta$ detection, indicating a $100-400$ Myr-old stellar population and high dust attenuation. BPT line ratios indicate the presence of an Active Galactic Nucleus (AGN). Decomposing narrow and broad line components, we recover broad, blueshifted H$\alpha$ with a velocity offset of $1245{\,\rm km\,s^{-1}}$ from the systemic narrow line velocity and with FWHM$\,\sim2500\,{\rm km\,s^{-1}}$. AzTEC-1's smooth morphology and stellar age is suggestive of a past merger-induced starburst period that would have brought in a second supermassive black hole, raising the possibility for a binary supermassive black hole system. In this scenario, we assume that the lower mass black hole hosts a broad line region orbiting a quiescent primary. Evidence for an extended outflow is not found in the 2D spectrum, NIRCam imaging, resolved ALMA observations of dust continuum, or CO, [C II]$_{157\,\mu \rm m}$ and [N II]$_{\rm 205\,\mu m}$ kinematics. AzTEC-1's high central gas mass surface density and dynamically unstable gas disk indicates that massive gas clouds external to the candidate binary SMBH's orbit might have played a role in stalling infall from $\sim10$ Myr to $\sim100$ Myr through dynamical torques, which has been theorized to occur in the nuclei of massive galaxies like AzTEC-1. If the supermassive black hole binary is confirmed, AzTEC-1 would be an excellent laboratory into the astrophysics driving low-frequency gravitational wave detections.
#### EWOCS-IX: JWST/NIRCam observations of Westerlund 2 - Identification of candidate substellar members
 - **Authors:** V. Almendros-Abad, M.G. Guarcello, K. Muzic, A. Scholz, M. Andersen, A. Bayo, W. Best, D. Capela, M. Gennaro, A. Ginsburg, J.B. Lovell, K. Monsch, E. Moraux, L. Prisinzano, T. Rom, E. Sabbi, P. Zeidler, C. Argiroffi, R. Bonito, D. Calzetti, V. Cusimano, F. Damiani, J.J. Drake, T.J. Haworth, N.D. Richardson, M. Robberto, S. Sciortino, N.J. Wright, T. Ziliotto
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2609.01880

 - **Pdf link:** https://arxiv.org/pdf/2609.01880

 - **Abstract**
 [Abridged] Investigating substellar populations in young massive clusters offers crucial insights into the formation of brown dwarfs (BDs) and the role of environmental conditions in shaping their properties. Westerlund 2 (Wd2), as one of the nearest dense and massive clusters in the Milky Way, represents an ideal laboratory for studying the effects of high stellar density and ionizing radiation from massive stars on BD formation. This paper presents deep JWST/NIRCam observations of Wd2 in a large number of filters between 1.15 and 4.1 $\mu m$. Our analysis focuses on identifying and characterizing the BD population within the cluster. We carried out PSF photometry on deep JWST/NIRCam data obtained in 4 wide and 6 medium-band filters, using DOLPHOT. The resulting catalog was used to identify BD candidates in Wd2 through spectral energy distribution (SED) fitting with atmospheric models. The 50\% detection limit of our NIRCam catalog is $\sim$0.015-0.02 $M_\odot$, at the distance, age, and extinction of Wd2, providing the deepest view of a supermassive star cluster to date. We identify 353 substellar candidates. Most candidates (301) lie above the 10 Myr isochrone in the Hertzsprung--Russell diagram consistent with cluster membership, which are defined as strong candidates. Comparison with a control field indicates a contamination level of $\lesssim$5\% for the strong candidate sample down to masses of $\sim$0.01--0.015~$M_\odot$. We identify 73 candidates exhibiting infrared excess indicative of circumstellar disks. These objects occupy the expected infrared-excess locus in de-reddened color diagrams and represent $27.7^{+3.4}_{-3.2}$\% of the candidates detected in F410M. The resulting catalog provides a well-characterized sample for future spectroscopic confirmation and subsequent studies of the substellar population of Wd2.
#### The GOGREEN Survey: AI Powered Deconvolution Lifts The Veil on Outside-in Environmental Quenching at z > 1
 - **Authors:** Aurelien Henry, Gillian Wilson, Gregory Rudnick, Pascale Jablonka, Utsav Akhaury, Craig Brooks, Michael Balogh, Ben Forrest, Adam Muzzin, Visal Sok, Mohamed H. Abdullah, M.E. Wisz, Elias Works
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2609.01903

 - **Pdf link:** https://arxiv.org/pdf/2609.01903

 - **Abstract**
 A powerful probe of the physical processes that quench star formation in dense environments is determining where within galaxies star formation is suppressed. At high redshift, the spatial resolution of multi-band imaging limits such measurements. We use deep-learning-based deconvolution to recover spatially resolved optical and near-infrared photometry for galaxies in nine GOGREEN clusters at 1<z<1.4, using customized models trained on HST and JWST imaging. Using resolved rest-frame UVJ colors, we classify galaxies by the star-forming states of their inner and outer regions into predominantly star-forming, predominantly quiescent, inside-quenched, or outside-quenched. We find that 24% of galaxies classified as quiescent from their integrated colors retain significant star formation. The predominantly quiescent fraction increases with stellar mass and is higher in clusters than in the field while the cluster quenched fraction excess is, when limiting to predominantly quenched galaxies, approximately 20%. Contrary to previous GOGREEN studies using integrated colors, we find this excess to be independent of stellar mass, demonstrating that partially quenched galaxies can bias measurements based on integrated colors. Among galaxies retaining significant star formation, outside-quenched galaxies are substantially more common than inside-quenched galaxies and have a fraction excess of (22.8+/-5.8)% in clusters relative to the field at low masses. This provides evidence that clusters preferentially suppress star formation in the outskirts of low-mass galaxies. Our results demonstrate the importance of spatially resolved classifications for interpreting environmental quenching at z~1 and the potential of deep-learning-based deconvolution to recover such information from large ground-based imaging datasets.
#### The Intermediate-Mass Black Hole Reverberation Mapping Project: Scientific Overview and Sample Characteristics
 - **Authors:** Hengxiao Guo, Jiancheng Wu, Wenwen Zuo, Ruining Tian, Xuechen Zheng, Meicun Hou, Paulina Lira, Philip G. Edwards, Vivian U, Shu Wang, Mar Mezcua, Luis C. Ho, Minfeng Gu, Tao An, Samuzal Barua, Colin J. Burke, Zhen-yi Cai, Xuheng Ding, Haicheng Feng, Alok C. Gupta, ShaSha Li, Wanling Liu, Wen-juan Liu, Ru-sen Lu, Dragana Ilić, Andjelka B. Kovačević, Yu Pan, Luka Č. Popović, Wenke Ren, Paula Sánchez-Sáez, Jamie Stevens, Jingbo Sun, Mouyuan Sun, Chizhuo Wang, Junxian Wang, Rongfeng Shen, Xuebing Wu, Yong Shi, Zhefu Yu, Zhenya Zheng, Ling Zhu
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2609.02179

 - **Pdf link:** https://arxiv.org/pdf/2609.02179

 - **Abstract**
 Recent discoveries with the James Webb Space Telescope of massive black holes at high redshift have highlighted fundamental questions about black hole seed formation and the coevolution of black holes with their host galaxies. Because the initial seed population cannot yet be observed directly, nearby intermediate-mass black holes provide a complementary fossil record of black hole formation and early growth. Motivated by this opportunity, we present the Intermediate-Mass Black Hole Reverberation Mapping (IMBH-RM) project and construct a homogeneous Sloan Digital Sky Survey sample of active broad-line IMBHs by uniformly reanalyzing literature candidates with consistent spectral decomposition and black hole mass estimation. Our sample contains 192 reliable IMBH candidates at $z\lesssim0.3$ with $\log(M_{\rm BH}/M_\odot)<6$, including four particularly compelling sources with $\log(M_{\rm BH}/M_\odot)<5$. The primary goal of IMBH-RM is to obtain reliable black hole masses from direct measurements and characteristic sizes of the broad-line region and accretion disk for a carefully selected subsample. These measurements will provide robust low-mass anchors for calibrating single-epoch black hole mass estimates and extending black hole--galaxy scaling relations into the IMBH regime. By building a statistically meaningful reverberation-mapped sample spanning $10^4-10^6\,M_\odot$, we aim to constrain the local IMBH mass distribution and place observational constraints on competing black hole seed formation scenarios. The future Multi-Channel Imager aboard the Chinese Space-station Survey Telescope provides a particularly promising platform for achieving these goals.
#### Scientific performances of the XGIS instrument on-board THESEUS
 - **Authors:** E. Arrigoni, S. Mereghetti, R. Campana, C. Labanti, A. Pisapia, P. Calabretto, G. Mattioli, E. Virgilli, L. Amati
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM)
 - **Arxiv link:** https://arxiv.org/abs/2609.02235

 - **Pdf link:** https://arxiv.org/pdf/2609.02235

 - **Abstract**
 The Transient High Energy Sky and Early Universe Surveyor (THESEUS) satellite, currently undergoing a Phase-A study for the M7 ESA mission selection, will mainly rely on the XGIS (X and Gamma Imaging Spectrometer) instrument to discover and precisely localise gamma-ray bursts and other high-energy transients. The XGIS instrument has been designed to provide accurate sky images in a wide field of view (>2 steradians) in the 2-150 keV band, coupled to coverage of nearly half of the sky with good timing and spectroscopic capabilities up to several MeV. This will be achieved thanks to the combination of two identical cameras, based on the coded mask imaging technique, oriented to provide partially overlapping fields of view. We present the capabilities of the XGIS, focussing in particular on the sensitivity and source location accuracy. We discuss the expected scientific advances in the GRB field, estimated through detailed Monte-Carlo simulations which take into account the design of the XGIS imaging system and the properties of the GRB population at high redshifts.


by ZhaoXu. 


2026-09-03
