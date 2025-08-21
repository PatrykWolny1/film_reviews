class Reviews {
    constructor() {
        this.modal = document.getElementById('addReviewModal');
        this.openBtn = document.getElementById('openAddReviewModal');
        this.closeBtn = document.querySelector('.close');
        this.form = document.getElementById('reviewForm');
        this.successMessage = document.getElementById('formSuccessMessage');

        this.setupEvents();
    }

    setupEvents() {
        if (this.openBtn) {
            this.openBtn.addEventListener('click', () => {
                this.modal.style.display = 'flex';
            });
        }

        if (this.closeBtn) {
            this.closeBtn.addEventListener('click', () => {
                this.closeModal();
            });
        }

        window.addEventListener('click', (event) => {
            if (event.target === this.modal) {
                this.closeModal();
            }
        });

        this.form.addEventListener('submit', (e) => {
            // Optional: comment out next line if you want real form submission
            // e.preventDefault();

            // Show success message
            this.successMessage.style.display = 'block';

            // Reset message after 2.5s
            setTimeout(() => {
                this.successMessage.style.display = 'none';
            }, 2500);
        });
    }

    closeModal() {
        this.modal.style.display = 'none';
        this.form.reset();
        this.successMessage.style.display = 'none';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    new Reviews();
});
