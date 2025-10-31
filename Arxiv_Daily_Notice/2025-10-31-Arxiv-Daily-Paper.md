# Showing new listings for Friday, 31 October 2025
Auto update Star Formation & Molecular Cloud papers at about 2:30am UTC (10:30am Beijing time) every weekday.


阅读 `Usage.md`了解如何使用此repo实现个性化的Arxiv论文推送

See `Usage.md` for instructions on how to personalize the repo. 


Keyword list: ['galaxy formation', 'satellite galaxy', 'Milky Way', 'TNG', 'EAGLE', 'COLIBRE', 'tidal disruption', 'small-scale structure', 'dwarf galaxy', 'N-body simulation', 'hydrodynamical simulation', 'cosmological simulation', 'dark matter halos', 'void', 'star cluster']


Excluded: ['interstellar medium', 'molecular cloud', 'standard candle', 'X-ray binar', 'solar corona', 'Instrumentation', 'planet']


### Today: 14papers 
#### Cosmological Simulations of Weakly Collisional Plasmas with Braginskii Viscosity in Galaxy Clusters
 - **Authors:** Tirso Marin-Gilabert, Ulrich P. Steinwandel, Milena Valentini, John A. ZuHone, Klaus Dolag
 - **Subjects:** Subjects:
Instrumentation and Methods for Astrophysics (astro-ph.IM); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Astrophysics of Galaxies (astro-ph.GA); Plasma Physics (physics.plasm-ph)
 - **Arxiv link:** https://arxiv.org/abs/2510.25847

 - **Pdf link:** https://arxiv.org/pdf/2510.25847

 - **Abstract**
 We present the implementation of an anisotropic viscosity solver within the magnetohydrodynamics (MHD) framework of the TreeSPH code OpenGadget3. The solver models anisotropic viscous transport along magnetic field lines following the Braginskii formulation and includes physically motivated limiters based on the mirror and firehose instability thresholds, which constrain the viscous stress in weakly collisional plasmas. To validate the implementation, we performed a suite of standard test problems -- including two variants of the sound-wave test, circularly and linearly polarized Alfven waves, fast magnetosonic wave, and the Kelvin-Helmholtz instability -- both with and without the plasma-instability limiters. The results show excellent agreement with the AREPO implementation of a similar anisotropic viscosity model (Berlok et al. 2019), confirming the accuracy and robustness of our method. Our formulation integrates seamlessly within the individual adaptive timestepping framework of OpenGadget3, avoiding the need for subcycling. This provides efficient and stable time integration while maintaining physical consistency. Finally, we applied the new solver to a cosmological zoom-in simulation of a galaxy cluster, demonstrating its capability to model anisotropic transport and plasma microphysics in realistic large-scale environments. Our implementation offers a versatile and computationally efficient tool for studying anisotropic viscosity in magnetized astrophysical systems.
#### Spiral Structure Diversity in Milky Way Analogs from TNG50: The Role of Gas and Disk Dynamics
 - **Authors:** Soumavo Ghosh, Elena D'Onghia
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.25848

 - **Pdf link:** https://arxiv.org/pdf/2510.25848

 - **Abstract**
 The generation of spiral arms and the mechanisms controlling their properties within a realistic cosmological framework - the complete understanding is still beyond our grasp. Using a statistically significant sample of Milky Way- and Andromeda-like (MW/M31) analogs from the high-resolution TNG50 cosmological simulation, we carry out the first systematic investigation of spiral-arm formation, their observable properties, and the underlying physical drivers. The selected analogs predominantly exhibit two-armed ($m = 2$) spirals in both stars and gas, while the gaseous disks often display stronger, more tightly wound, and multi-armed patterns ($m>2$). Spiral features appear across stellar populations of different ages, confirming their density-wave nature and producing coherent spirals in both metallicity and mean stellar age distributions-consistent with recent Gaia observations of the Milky Way. Our analysis reveals a diverse dynamical scenario for spiral generation: gas content, disk coldness, and shear jointly regulate the growth and morphology of spiral perturbations. We find that the gas content and the dynamical coldness of the disk jointly regulate spiral growth: galaxies with higher gas fractions and colder disks develop more prominent spirals. The measured relation between spiral pitch angle and disk shear shows significant scatter around the analytic prediction, likely due to the combined influence of bars, gas inflows, and feedback. These results demonstrate that spiral density waves can persist in fully cosmological disks, linking internal dynamical processes to galaxy assembly and offering testable predictions for present and future surveys such as JWST and Roman.
#### Mitigating gain calibration errors from EoR observations with SKA1-Low AA*
 - **Authors:** Eeshan Beohar, Abhirup Datta, Anshuman Tripathi, Samit Kumar Pal, Rashmi Sagar
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/2510.25886

 - **Pdf link:** https://arxiv.org/pdf/2510.25886

 - **Abstract**
 The observation of the redshifted 21-cm signal from neutral hydrogen is a promising probe for understanding the phase transition of the early universe and its evolution during the Cosmic Dawn and the Epoch of Reionisation (EoR). One of the primary obstacles to the statistical detection of the target signal is the presence of residual foreground, which arises from gain calibration errors. Previous studies have shown that gain calibration errors as small as 0.01% can lead to a biased interpretation of the observed signal power spectrum estimation, by nearly an order of magnitude. A recent study further highlights that to retrieve astrophysical parameters accurately, the threshold gain calibration error should be lower than 0.01%. In this work, we develop a post-calibration mitigation strategy that combines foreground subtraction techniques with foreground avoidance to address residual contamination arising from gain calibration errors. We use an end-to-end pipeline 21cmE2E to simulate a realistic sky model and telescope configuration within the 138-146 MHz frequency range. To assess the impact of residual antenna-based gain calibration errors, we perform a detailed power spectrum analysis across several threshold levels. Our analysis shows that the extraction of the target signal over the wavenumber range $0.05 \leq k \leq 0.5$ Mpc$^{-1}$ is possible with a threshold gain calibration error of 1%, although with a significant SNR tradeoff on larger scales. Moreover, this work also offers a comparative assessment of foreground removal and avoidance techniques in the context of future SKA1-Low AA* observations.
#### Lyman-$α$ radiation pressure regulates star formation efficiency
 - **Authors:** D. Manzoni, A. Ferrara
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.25950

 - **Pdf link:** https://arxiv.org/pdf/2510.25950

 - **Abstract**
 Order-unity star formation efficiencies (SFE) in early galaxies may explain the overabundance of bright galaxies observed by JWST at high redshift. Here we show that Lyman-$\alpha$ (Ly$\alpha$) radiation pressure limits the gas mass converted into stars, particularly in primordial environments. We develop a shell model including Ly$\alpha$ feedback, and validate it with one-dimensional hydrodynamical simulations. To account for Ly$\alpha$ resonant scattering, we adopt the most recent force multiplier fits, including the effect of Ly$\alpha$ photon destruction by dust grains. We find that, independently of their gas surface density $\Sigma_g$, clouds are disrupted on a timescale shorter than a free-fall time, and even before supernova explosions if $\Sigma_g \gtrsim 10^3\,M_{\odot}\ \rm pc^{-2}$. At $\log(Z/Z_{\odot}) = -2$, relevant for high-redshift galaxies, the SFE is $0.01 \lesssim \hat{\epsilon}_{*} \lesssim 0.66$ for $10^3 \lesssim\Sigma_g [M_{\odot}\ \rm pc^{-2}] \lesssim 10^5$. The SFE is even lower for decreasing metallicity. Near-unity SFEs are possible only for extreme surface densities, $\Sigma_{g} \gtrsim 10^5\;M_{\odot}\ \rm pc^{-2}$, and near-solar metallicities. We conclude that Ly$\alpha$ radiation pressure severely limits a possible extremely efficient, feedback-free phase of star formation in dense, metal-poor clouds.
#### Shock-driven heating in the circumnuclear star-forming regions of NGC 7582: Insights from JWST NIRSpec and MIRI/MRS spectroscopy
 - **Authors:** Oscar Veenema, Niranjan Thatte, Dimitra Rigopoulou, Ismael García-Bernete, Almudena Alonso-Herrero, Anelise Audibert, Enrica Bellocchi, Andrew J. Bunker, Steph Campbell, Francoise Combes, Ric I. Davies, Daniel Delaney, Fergus Donnan, Federico Esposito, Santiago García-Burillo, Omaira Gonzalez Martin, Laura Hermosa Muñoz, Erin K. S. Hicks, Sebastian F. Hoenig, Nancy A. Levenson, Chris Packham, Miguel Pereira-Santaella, Cristina Ramos Almeida, Claudio Ricci, Rogemar A. Riffel, David Rosario, Lulu Zhang
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26321

 - **Pdf link:** https://arxiv.org/pdf/2510.26321

 - **Abstract**
 We present combined JWST NIRSpec and MIRI/MRS integral field spectroscopy data of the nuclear and circumnuclear regions of the highly dust obscured Seyfert 2 galaxy NGC 7582, which is part of the sample of AGN in the Galaxy Activity, Torus and Outflow Survey (GATOS). Spatially resolved analysis of the pure rotational H$_2$ lines (S(1)-S(7)) reveals a characteristic power-law temperature distribution in different apertures, with the two prominent southern star-forming regions exhibiting unexpectedly high molecular gas temperatures, comparable to those in the AGN powered nuclear region. We investigate potential heating mechanisms including direct AGN photoionisation, UV fluorescent excitation from young star clusters, and shock excitation. We find that shock heating gives the most plausible explanation, consistent with multiple near- and mid-IR tracers and diagnostics. Using photoionisation models from the PhotoDissociation Region Toolbox, we quantify the ISM conditions in the different regions, determining that the southern star-forming regions have a high density ($n_H \sim 10^{5}$ cm$^{-3}$) and are irradiated by a moderate UV radiation field ($G_0 \sim 10^{3}$ Habing). Fitting a suite of Paris-Durham shock models to the rotational H$_2$ lines, as well as rovibrational 1-0 S(1), 1-0 S(2), and 2-1 S(1) H$_2$ emission lines, we find that a slow ($v_s \sim 10$ km/s) C-type shock is likely responsible for the elevated temperatures. Our analysis loosely favours local starburst activity as the driver of the shocks and circumnuclear gas dynamics in NGC 7582, though the possibility of an AGN jet contribution cannot be excluded.
#### Tracing the evolution of brightest galaxies and diffuse light in galaxy groups
 - **Authors:** B. Bilata-Woldeyes, J. D. Perea, J. M. Solanes
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26329

 - **Pdf link:** https://arxiv.org/pdf/2510.26329

 - **Abstract**
 We present a suite of 100 cosmologically motivated, controlled N-body simulations designed to advance the understanding of the role of purely gravitational dynamics in the early formation of low-mass galaxy groups (~ 1-5 x 10^13 M_sun). In this work, we investigate the temporal evolution of key indicators of dynamical relaxation, with particular emphasis on the secular growth of the diffuse intragroup light (IGL), the four major group galaxies, and the mass distributions of their progenitors. We also assess the diagnostic power of several magnitude gaps between top-ranked galaxies as proxies for dynamical age. As in our previous study, we compare outcomes from three group classes defined by the number of brightest group galaxies (BGGs) present at the end of the simulations. The early assembly of galaxy groups is consistent with a stochastic Poisson process at an approximately constant merger rate. Various dynamical diagnostics - including galaxy pairwise separations, velocity dispersions, and the offset of the first-ranked galaxy from the group barycentre - indicate that single-BGG groups evolve more rapidly towards virialisation than double- and especially non-BGG systems. We further find that first-ranked group members and the IGL, follow distinct growth histories, with the IGL assembled from a more numerous and systematically lower-mass population than the central object. This distinction is particularly pronounced in non-BGG systems, where about one third of the IGL originates from small galaxies, each contributing less than 5% to this component. Among the tested magnitude gaps, the difference between the first- and fourth-ranked galaxies, $\Delta M4-1$, proves a more robust indicator of dynamical age for low-mass groups than the conventional $\Delta M2-1$ gap. The $\Delta M5-1$ and $\Delta M6-1$ gaps also perform well and may be preferable in certain contexts.
#### oMEGACat. VIII. A Subpopulation Census of ω Centauri
 - **Authors:** C. Clontz, A. C. Seth, Z. Wang, M. Haeberle, M. S. Nitschai, N. Neumayer, P. J. Smith, M. Latour, A. Feldmeier-Krause, M. Libralato, A. Bellini
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26341

 - **Pdf link:** https://arxiv.org/pdf/2510.26341

 - **Abstract**
 An understanding of the assembly history of the complex star cluster Omega Centauri has long been sought after, with many studies separating the stars on the color-magnitude diagram into multiple groupings across small magnitude ranges. Utilizing the oMEGACat combined astro-photometric and spectroscopic dataset we parse 14 subpopulations from the upper red-giant branch to below the main-sequence turnoff. We combine our results with previous works to estimate the age and age spread of each population. We find that the chemically enhanced (P2) populations are all ~1 Gyr younger (~11.6 Gyr old) and have significantly higher intrinsic age spreads (0.6 Gyr) than the primordial (P1) populations (~12.6 Gyr old, 0.3 Gyr spread), with the intermediate (Im) populations falling in between the two. Additionally, we connect for the first time the Chromosome Diagram to the two-stream age-metallicity relation, allowing us to link the P1 and P2 stars to the distinct star formation tracks, proposed to be in-situ and ex-situ contributions to the cluster's assembly. Our results are consistent with some suggested formation models and rule out others but no current model can explain all observed features of the subpopulations.
#### The rotation speed of the spiral pattern in the Milky Way galaxy
 - **Authors:** Vadim V. Bobylev, Anisa T. Bajkova, Anton A. Smirnov
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26450

 - **Pdf link:** https://arxiv.org/pdf/2510.26450

 - **Abstract**
 For a sample of masers, the basic kinematic equations were solved by including the Galactic rotation parameters and the peculiar velocity of the Sun as the unknown variables. Based on spectral analysis, the following estimates were obtained: $|f|_{R,\theta}=(7.0,5.1)\pm(1.2,1.4)$ km s$^{-1}$ and the corresponding wavelengths $\lambda_{R,\theta}=(1.9,1.7)\pm(0.4,0.7)$ kpc, as well as $\chi_\odot=-140^\circ\pm15^\circ$. The presence of periodic perturbations in the vertical velocities of masers with an amplitude of $|f|_W=3.1\pm1.4$ km s$^{-1}$ and a wavelength of $\lambda=1.9\pm0.8$ kpc was confirmed. It is shown that the velocities $f_R$ and $f_\theta$ can have both the same and different signs. Therefore, we obtained a large scatter of estimates. Thus, if $f_R$ and $f_\theta$ have the same signs, then $\Omega_p=25.8\pm2.0$ km s$^{-1}$ kpc$^{-1}$ and $R_{cor}=9.1\pm0.8$ kpc. And when $f_R$ and $f_\theta$ have different signs, then $\Omega_p=35.4\pm2.0$ km s$^{-1}$ kpc$^{-1}$ and $R_{cor}=6.8\pm0.8$ kpc.
#### A test of invariance of halo surface density for FIRE-2 simulations with cold dark matter and self-interacting dark matter
 - **Authors:** Sujit K. Dalui, Shantanu Desai
 - **Subjects:** Subjects:
Cosmology and Nongalactic Astrophysics (astro-ph.CO)
 - **Arxiv link:** https://arxiv.org/abs/2510.26545

 - **Pdf link:** https://arxiv.org/pdf/2510.26545

 - **Abstract**
 Numerous observations have shown that the dark matter halo surface density, defined as the product of core radius and halo central density of cored dark matter haloes is nearly constant and independent of galaxy mass over a whole slew of galaxy types. Here we calculate the surface density in cold dark matter(CDM) and self-interacting dark matter (SIDM) models including baryons, as well as SIDM without baryons, for dwarf galaxies of masses $\approx 10^{10} M_{\odot}$ using mock catalogs obtained from simulations as part of the Feedback In Realistic Environments project. We find that the dark matter surface density and column density are nearly constant for CDM and SIDM for this mass range. The halo surface density obtained from the Burkert profile fit is consistent with galactic-scale observations within $1\sigma$. We also computed the empirical scaling relations between the central surface density and maximum velocity using the best-fit dark matter profiles, and found that they agree with observations of Milky Way and M31 dwarfs.
#### A Star's Death by a Thousand Cuts: The Runaway Periodic Eruptions of AT2023uqm
 - **Authors:** Yibo Wang, Tingui Wang, Shifeng Huang, Jiazheng Zhu, Ning Jiang, Wenbin Lu, Rongfeng Shen, Shiyan Zhong, Dong Lai, Yi Yang, Xinwen Shu, Tianyu Xia, Di Luo, Jianwei Lyu, Thomas Brink, Alex Filippenko, Weikang Zheng, Minxuan Cai, Zelin Xu, Mingxin Wu, Xiaer Zhang, Weiyu Wu, Lulu Fan, Ji-an Jiang Xu Kong, Bin Li, Feng Lin, Ming Liang, Wentao Luo, Jinlong Tang, Zhen Wan, Hairen Wang, Jian Wang, Yongquan Xue, Dazhi Yao, Hongfei Zhang, Wen Zhao, Xianzhong Zheng, Qingfeng Zhu, Yingxi Zuo
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE)
 - **Arxiv link:** https://arxiv.org/abs/2510.26561

 - **Pdf link:** https://arxiv.org/pdf/2510.26561

 - **Abstract**
 Stars on bound orbits around a supermassive black hole may undergo repeated partial tidal disruption events (rpTDEs), producing periodic flares. While several candidates have been suggested, definitive confirmation of these events remains elusive. We report the discovery of AT2023uqm, a nuclear transient that has exhibited at least five periodic optical flares, making it only the second confirmed case of periodicity after ASASSN-14ko. Uniquely, the flares from AT2023uqm show a nearly exponential increase in energy--a "runaway" phenomenon signaling the star's progressive destruction. This behavior is consistent with rpTDEs of low-mass, main-sequence stars or evolved giant stars. Multiwavelength observations and spectroscopic analysis of the two most recent flares reinforce its interpretation as an rpTDE. Intriguingly, each flare displays a similar double-peaked structure, potentially originating from a double-peaked mass fallback rate or two discrete collisions per orbit. The extreme ratio of peak separation to orbital period draws attention to the possibility of a giant star being disrupted, which could be distinguished from a low-mass main-sequence star by its future mass-loss evolution. Our analysis demonstrates the power of rpTDEs to probe the properties of disrupted stars and the physical processes of tidal disruption, though it is currently limited by our knowledge of these events. AT2023uqm emerges as the most compelling rpTDE thus far, serving as a crucial framework for modeling and understanding these phenomena.
#### The chemical DNA of the Magellanic Clouds IV. Unveiling extreme element production: the Eu abundance in the Small Magellanic Cloud
 - **Authors:** Samuele Anoardo, Alessio Mucciarelli, Marco Palla, Lorenzo Santarelli, Carmela Lardo, Donatella Romano
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR)
 - **Arxiv link:** https://arxiv.org/abs/2510.26625

 - **Pdf link:** https://arxiv.org/pdf/2510.26625

 - **Abstract**
 In this study we investigate the chemical enrichment of the rapid neutron-capture process in the Small Magellanic Cloud (SMC). We measure [Eu/Fe] abundance ratios in 209 giant stars that are confirmed members of the SMC, providing the first extensive dataset of Eu abundances in this galaxy across its full metallicity range, spanning more than 1.5 dex. We compare Eu abundances with those of Mg and Ba to evaluate the efficiency of the r-process relative to $\alpha$-capture and s-process nucleosynthesis. The SMC shows enhanced [Eu/Fe] values at all metallicities (comparable with the values measured in the Milky Way), with a clear decline as [Fe/H] increases (from $\sim$ -1.75 dex to $\sim$ -0.5 dex), consistent with the onset of Type Ia supernovae. In contrast, [Eu/Mg] is enhanced by about +0.5 dex at all [Fe/H], significantly above the values observed in Milky Way stars, where [Eu/Mg] remains close to solar, reflecting comparable production of r-process and $\alpha$-capture elements. Moreover, [Ba/Eu] increases with metallicity, beginning at [Fe/H] $\approx$ -1.5 dex, namely at a lower metallicity with respect to the Milky Way, where [Ba/Eu] starts to increase around [Fe/H] $\approx$ -1 dex. Our findings suggest the SMC has a higher production of Eu (with respect to the $\alpha$-elements) than the Milky Way but in line with what observed in other dwarf systems within the Local Group. We confirm that galaxies with star formation efficiencies lower than the Milky Way have high [Eu/$\alpha$], probably indicating a stronger efficiency of the delayed sources of r-process at low metallicities.
#### Tidal disruption events with SPH-EXA: resolving the return of the stream
 - **Authors:** Noah Kubli, Alessia Franchini, Eric R. Coughlin, C. J. Nixon, Sebastian Keller, Pedro R. Capelo, Lucio Mayer
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26663

 - **Pdf link:** https://arxiv.org/pdf/2510.26663

 - **Abstract**
 In a tidal disruption event (TDE), a star is disrupted by the tidal field of a massive black hole, creating a debris stream that returns to the black hole, forms an accretion flow, and powers a luminous flare. Over the last few decades, several numerical studies have concluded that shock-induced dissipation occurs as the stream returns to pericentre (i.e., pre-self-intersection), resulting in efficient circularisation of the debris. However, the efficacy of these shocks is the subject of intense debate. We present high-resolution simulations (up to 10^10 particles) of the disruption of a solar-like star by a 10^6M_sun black hole with the new, GPU-based, smoothed-particle hydrodynamics code SPH-EXA, including the relativistic apsidal precession of the stellar debris orbits; our simulations run from initial disruption to the moment of stream self-intersection. With 10^8 particles - corresponding to the highest-resolution SPH simulations of TDEs in the pre-existing literature - we find significant, in-plane spreading of the debris as the stream returns through pericenter, in line with previous works that suggested this is a significant source of dissipation and luminous emission. However, with increasing resolution this effect is dramatically diminished, and with 10^10 particles there is effectively no change between the incoming and the outgoing stream widths. Our results demonstrate that the paradigm of significant dissipation of kinetic energy during pericentre passage is incorrect, and instead it is likely that debris circularisation is mediated by the originally proposed, stream-stream collision scenario.
#### Active Dwarf Galaxy Database II: Connections between Host Galaxy Properties and Black Hole Accretion Signatures
 - **Authors:** Erik J. Wasleske, Vivienne F. Baldassare, Christopher M. Carroll
 - **Subjects:** Subjects:
Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26716

 - **Pdf link:** https://arxiv.org/pdf/2510.26716

 - **Abstract**
 We investigate the connection between accretion signatures and host galaxy properties in the context of how active dwarf galaxies are identified. We use the database constructed in Wasleske & Baldassare (2024) which contains dwarf galaxies that were selected as active galaxies by optical spectroscopy, infrared colors, X-ray brightness, and photometric variability. Multi-wavelength archival data was used to consistently apply all of these methods to every galaxy within this compiled set. The cross application of these methods resulted in a diversity of sub-populations identified as active by some set of these techniques. In this paper, we estimate host galaxy properties from spectral energy distribution models. We connect the active galactic nuclei (AGN) signatures to our estimated host galaxies' properties using statistical dimensionality reduction methods. We find that dwarf AGN selected by infrared colors are the most distinct population, with the highest star formation rates and lowest stellar masses. We also find some other key population differences, such as the broad line AGN having significantly higher AGN luminosities. X-ray and variability selected AGN have higher average star formation rates than those selected with optical narrow line spectroscopic diagrams. Our connections to the host galaxy parameters potentially point to the sub-populations representing different epochs of the evolution of accretion.
#### Compact Accretion Disks in the Aftermath of Tidal Disruption Events: Parameter Inference from Joint X-ray Spectra and UV/Optical Photometry Fitting
 - **Authors:** M. Guolo, A. Mummery, S. van Velzen, S. Gezari, M. Nicholl, Y. Yao, M. Karmen, Y. Ajay, T. Wevers, N. LeBaron, R. Chornock
 - **Subjects:** Subjects:
High Energy Astrophysical Phenomena (astro-ph.HE); Astrophysics of Galaxies (astro-ph.GA)
 - **Arxiv link:** https://arxiv.org/abs/2510.26774

 - **Pdf link:** https://arxiv.org/pdf/2510.26774

 - **Abstract**
 We present a multi-wavelength analysis of 14 tidal disruption events (TDEs)-including an off-nuclear event associated with an ultra-compact dwarf galaxy-selected for having available thermal X-ray spectra during their late-time UV/optical plateau phase. We show that at these stages, the full spectral energy distribution - X-ray spectra and UV/optical photometry - is well described by a compact, yet standard accretion disk, the same disk which powers the X-rays at all times. By fitting up to three three epochs per source with a fully relativistic disk model, we show that many system properties can be reliably recovered, including importantly the black hole mass ($M_{\bullet}$). These accretion-based $M_{\bullet}$ values, which in this sample span nearly three orders of magnitude, are consistent with galactic scaling relations but are significantly more precise (68\% credible interval $ < \pm 0.3$ dex) and physically motivated. Expected accretion scaling relations (e.g., $L_{Bol}^{ disk} / L_{Edd} \propto T_p^4 \propto M_{\bullet}^{-1}$), TDE-specific physics correlations ($L_{plat} \propto M_{\bullet}^{2/3}$ and $R_{out}/r_g \propto M_{\bullet}^{-2/3}$) and black hole-host galaxy correlations ($M_{\bullet}$-$M_{\star}$ and $M_{\bullet}$-$\sigma_{\star}$) naturally emerge from the data and, for the first time, are self-consistently extended into the intermediate-mass (IMBH, $M_{\bullet} < 10^{5}$) regime. We discuss the implications of these results for TDE physics and modeling. We also review and discuss different methods for $M_{\bullet}$ inference in TDEs, and find that approaches based on physical models of the early-time UV/optical emission are not able to recover (at a statistically significant level) black hole-host galaxy scalings.


by ZhaoXu. 


2025-10-31
