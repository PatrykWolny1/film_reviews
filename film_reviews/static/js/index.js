class Index {
    constructor() {
        this.films = {
            'cleaner': {
                title: "Cleaner",
                description: "A suspense-filled thriller, 'Cleaner' follows the life " +
                              "of Tom Cutler, a former police officer who now runs " +
                              "a crime scene cleanup business. Caught in a web of deceit " +
                              "after cleaning up an undiscovered crime scene, Tom must " +
                              "navigate corruption and cover-ups to protect his family " +
                              "and clear his name.",
                rating: "Rating: ★★★☆☆"
            },
            'duplicity': {
                title: "Duplicity",
                description: "Romantic spy thriller revolving around two ex-agents turned " +
                              "corporate spies, embroiled in high-stakes espionage while " +
                              "untangling their complicated feelings for each other.",
                rating: "Rating: ★★★★☆"
            },
            'zzone': {
                title: "ZZone",
                description: "Set in a dystopian future, 'ZZone' explores the aftermath " +
                              "of a global pandemic, with survivors fending off zombie-like " +
                              "creatures and human adversaries within a fortified zone.",
                rating: "Rating: ★★★☆☆"
            },
            'counterstrike': {
                title: "Counterstrike",
                description: "An action-packed military thriller about an elite counter-terrorism " +
                              "squad's mission across continents to thwart a terrorist plot " +
                              "against major world cities.",
                rating: "Rating: ★★★★★"
            }
        };
        this.setupEventListeners();
        this.isVisible = false; // Track the visibility of the details pane
    }

    setupEventListeners() {
        const thumbnails = document.querySelectorAll('.movie-thumbnails img');
        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener('click', (event) => this.toggleMovieDetails(event.target));
        });
    }

    toggleMovieDetails(img) {
        const movieDetails = document.querySelector('.movie-details');
        const movieImage = document.querySelector('.movie-image');
        const movieTitle = document.querySelector('.movie-title');
        const movieDescription = document.querySelector('.movie-description');
        const movieRating = document.querySelector('.movie-rating');
        const filmKey = img.alt.toLowerCase(); // Use the alt text to identify the film

        if (this.isVisible) {
            movieDetails.style.display = 'none';
            this.isVisible = false;
        } else {
            // Update image and details using the films data object
            const filmData = this.films[filmKey];
            movieImage.src = img.src;
            movieImage.alt = filmData.title;
            movieTitle.textContent = filmData.title;
            movieDescription.textContent = filmData.description;
            movieRating.textContent = filmData.rating;

            movieDetails.style.display = 'flex';
            this.isVisible = true;
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    new Index();
});
