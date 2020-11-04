# Expanded Archive

Repository for the Jupyter Notebooks, Python and JSON files for the Expanded Archive Project, an attempt for curating an art exhibition using Machine Learning.

This project assumes the two fundamental roles of an art curator:
1. Exploring, reviewing and selecting artworks (images) from her/his own personal archives, galleries, museums, etc.
2. Reading, highlighting and selecting relevant ideas from text, publications and discussions surrounding art and their artists.

Under this framework, the role of the curator can be interpreted in computational terms as someone that organizes and selects content from various text and image datasets. Using Machine Learning models for text vectorization and image recognition, I recreated a model which follows these steps in order to curate an art-show:

- Scrape an Image collection, in this case the [Open Access Metropolitan Museum of Art Highlight Artworks](https://metmuseum.github.io/)
- Scrape the text from around 60 exhibition catalogues from [MetPublications](https://www.metmuseum.org/art/metpublications)
- Scrape the images from Instagram Accounts of around 50 contemporary artists
- Scrape the text of said contemporary artists from their websites or Instagram posts.

Once this information is obtained, Word2Vec is used for text vectorization, assembling a list of keywords for both the collection and artist's texts. VGG16 is used for image recognition. Then, similarity and distance calculations were performed on both values, and a ranking assembled in which the artworks at the top are assumed to be more closely related to the Museum's collection, thus 'curated' by the collection.
