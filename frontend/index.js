// AI Grammar Tutor Application
class GrammarTutor {
    constructor() {
        this.currentView = 'landing';
        this.messages = [];
        this.apiUrl = "http://localhost:8000/api/grammar"; // Change if backend is hosted elsewhere
        this.init();
    }

    init() {
        this.bindEvents();
    }

    bindEvents() {
        // Navigation between landing and chat
        document.getElementById('start-learning-btn').addEventListener('click', () => {
            this.showChatInterface();
        });

        document.getElementById('start-journey-btn').addEventListener('click', () => {
            this.showChatInterface();
        });

        document.getElementById('back-to-landing').addEventListener('click', () => {
            this.showLandingPage();
        });

        // Message form submission
        document.getElementById('message-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleMessageSubmit();
        });

        // Enter key support
        document.getElementById('message-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.handleMessageSubmit();
            }
        });
    }

    showChatInterface() {
        document.getElementById('landing-page').classList.add('hidden');
        document.getElementById('chat-interface').classList.remove('hidden');
        this.currentView = 'chat';
        
        // Focus on input
        setTimeout(() => {
            document.getElementById('message-input').focus();
        }, 100);
    }

    showLandingPage() {
        document.getElementById('chat-interface').classList.add('hidden');
        document.getElementById('landing-page').classList.remove('hidden');
        this.currentView = 'landing';
    }

    async handleMessageSubmit() {
        const input = document.getElementById('message-input');
        const message = input.value.trim();
        if (!message) return;

        // Add user message
        this.addMessage(message, 'user');
        // Clear input
        input.value = '';
        // Show typing indicator
        this.showTypingIndicator();

        try {
            // Call API to get AI response
            const aiResponse = await this.fetchGrammarResponse(message);
            this.hideTypingIndicator();
            this.addMessage(aiResponse, 'ai');
        } catch (err) {
            this.hideTypingIndicator();
            this.addMessage("Sorry, I couldn't process your request. Please try again.", 'ai');
        }
    }

    async fetchGrammarResponse(text) {
        const response = await fetch(this.apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });
        if (!response.ok) throw new Error("API error");
        const data = await response.json();
        return data.result;
    }

    addMessage(content, sender) {
        const messagesContainer = document.getElementById('messages-container');
        const messageDiv = document.createElement('div');
        
        if (sender === 'user') {
            messageDiv.className = 'flex items-start space-x-3 justify-end message-enter';
            messageDiv.innerHTML = `
                <div class="bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg p-4 shadow-soft max-w-md">
                    <p>${this.escapeHtml(content)}</p>
                </div>
                <div class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center flex-shrink-0" aria-label="User">
                    <svg class="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                    </svg>
                </div>
            `;
        } else {
            messageDiv.className = 'flex items-start space-x-3 message-enter';
            messageDiv.innerHTML = `
                <div class="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full flex items-center justify-center flex-shrink-0" aria-label="AI">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                    </svg>
                </div>
                <div class="bg-white rounded-lg p-4 shadow-soft max-w-md">
                    <p class="text-gray-800" style="white-space: pre-line;">${this.escapeHtml(content)}</p>
                </div>
            `;
        }
        
        messagesContainer.appendChild(messageDiv);
        // Always scroll to bottom after adding a message
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        // Store message
        this.messages.push({ content, sender, timestamp: new Date() });
    }

    showTypingIndicator() {
        document.getElementById('typing-indicator').classList.remove('hidden');
        const messagesContainer = document.getElementById('messages-container');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    hideTypingIndicator() {
        document.getElementById('typing-indicator').classList.add('hidden');
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the application and effects when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new GrammarTutor();

    // Add parallax effect to hero section (if present)
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.animate-slide-up');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.1}px)`;
        }
    });
    
    // Add hover effects to feature cards
    const featureCards = document.querySelectorAll('.animate-fade-in-scale');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'scale(1.05) translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'scale(1) translateY(0)';
        });
    });
});