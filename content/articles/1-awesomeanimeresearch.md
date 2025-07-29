Title: AwesomeAnimeResearch: Past, Present, and Future
Date: 2022-11-24
Tags: cs
Category: cs
Slug: 1-awesomeanimeresearch
Authors: lento

## Introduction
I have created and managed a repository, named [AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) for more than two years (the first commit was at 04/27/2020). Thanks to contributors and issue builders, we have collected more than 250 papers related to anime, illustration, and comic. I would like to explain motivation to create the repository, design, present challenges, and future plans.

## Motivation
Until I created the repository, I used to take a look at [DeepLearningAnimePapers](https://github.com/shubhampachori12110095/DeepLearningAnimePapers) to investigate papers related to anime. Since it had stopped updates in 2018, I had possessed a desire to create awesome-list for anime papers that contains a massive and exciting collection. Therefore, [I started to manage AwesomeAnimeResearch](https://twitter.com/NieA7_3170/status/1258700433356283910?s=20&t=PrGYp5veSVDrUamtQqjMCg).

## Design
- In the first place, what is the definition of "papers related to anime, illustration, and comic"? I have defined it as the published or preprint papers that explicitly include applications for these fields. For example, if the paper is about image generation and includes the generated figures of not only human faces but also anime characters, the paper clearly shows potentials for anime applications. Of course, since the definition is from all my perspectives, I am willing to discuss the appropriate definition.
- There are 2 categories of resources in AwesomeAnimeResearch: paper and project. Papers are the papers in accordance with the definition that I stated. Projects are not the papers but they are tech reports or github repositories that have contributed to promoting machine learning research related to anime (e.g. [makegirlsmoe](https://make.girls.moe/#/) or [style2paints](https://github.com/lllyasviel/style2paints)). 
- I have set 21 categories like below based on my perspective, and four categories have their own subcategories.

```
- Dataset
- Image Generation
  |- Generation
  |- Few-shot
  |- Interpretability
  |- Montage
- Image-to-Image Translation
  |- Face2anime
  |- Selfie2anime
  |- Photo2anime
  |- Sketch2anime
  |- Photo2manga
  |- Anime2costume
  |- Style transfer
  |- Author style transfer
- Automatic Line Art Colorization
  |- NoHint
  |- Atari
  |- Reference
  |- Tag
  |- Video
- Automatic Character Lighting
- Automatic Illustration Editing
- Automatic Sketch Editing
- Automatic Animation Inbetweening
- Automatic Image Enhancement
- Character Animating
- Manga Application
  |- Generation
  |- Restoration
  |- Inpainting
  |- Text detection
  |- Landmark detection
  |- Segmentation
  |- Translation
  |- Depth estimation
  |- Vectorization
  |- Re-identification
- Representation Learning
- Pose Estimation
- Image Retrieval
- Visual Correspondence
- Character Recognition
- 3D Character Creation
- Robotics
- Speech Synthesis
- Adult Content Detection
- Survey
```

- When it comes to the papers, each record has three or four fields depending on the existence of subcategories.

```
- Subcategory (optional): if the category does not have subcategories, this field does not exist
- Paper (required): The link and the name of the paper
- Conference (optional): The abbreviated form of the conference name including the year
- Links (optional): Webpages describing the paper aside from the published paper (e.g. a Github repository or a specific webpage). Multiple sources are OK
```

- As for the projects, each record has the link and the name of the project. If the project is about the tech report and the webpage, the title is treated as the name. If the project is about the github repository, a combination of the username and the name of the repository corresponds to the name.

## Present Challenges
- Diversity
    - There are two aspects about the diversity: number of papers and uniqueness.
        - Number of papers: I have noticed that the current version of AwesomeAnimeResearch lacks papers among several categories. Some categories include abundant papers, and others do not. I have to admit that the lack comes from my interests. Although several issue builders and contributers have mitigated the problem, there seems still be imbalanced with respect to the number of papers. Moreover, the categorization that I showed in the design section is not expected for researchers working on speech processing and natural language processing because the current categories lack papers related to the areas.
        - Uniqueness: Papers among some categories would be overabundant because several pairs of the papers in one category mostly resemble each other. The truncation would be imperative to enable users to access to the desired paper faster.
- Completeness
    - A lot of dead links for the paper and blanks in the conference name exist. Especially as for the former problem, it significantly decreases the accessibility of users.

## Future Plans
I will continue to add papers and projects to the repository via a search in reddit and google scholar. I also always accept issues and PR from others. Especially the latter leads to mitigating the problems of diversity. On the other hand, I am thinking about creating the script to search papers related to each category. This script would not only solve the problem of dead links and blanks but also enhance the objectiveness in searching the papers. If you have questions, corrections, or suggestions, I am willing to welcome and discuss them via Github Issue.