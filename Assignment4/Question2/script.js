function getJSONPQuote() {
    // Generate a unique callback name for each request
    const callbackName = 'forismaticCallback_' + new Date().getTime();

    window[callbackName] = function(data) {
        const quoteText = data.quoteText;
        const quoteAuthor = data.quoteAuthor || "Unknown";
        document.getElementById('quote-display').innerHTML = `<p>"${quoteText}"</p><p>- ${quoteAuthor}</p>`;

        // Clean up: Remove the script tag after receiving the response
        document.body.removeChild(document.getElementById(callbackName));
        // Clean up: Delete the callback function
        delete window[callbackName];
    };

    const script = document.createElement('script');
    script.id = callbackName; // Use the unique callback name as the ID
    script.src = `https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=${callbackName}`;
    document.body.appendChild(script);
}

let debounceTimeout;

document.getElementById('new-quote').addEventListener('click', () => {
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(getJSONPQuote, 300); // 300 ms debounce period
});
