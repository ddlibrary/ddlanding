/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/*.html",
        "./node_modules/flowbite/**/*.js",
    ],
    theme: {
        extend: {
            colors: {
                'duron-mindful-gray': '#c8bfb6',
                'shade-of-red': '#aa6562',
                'different-shade-of-red': '#e2625c',
                'shade-of-orange': '#e66019',
                'very-light-shade-of-orange': '#f0eae5',
                'very-dark-shade-of-orange': '#772b02',
                'shade-of-green': '#9fbd9a',
                'shade-of-brown': '#796a58',
                'different-shade-of-brown': '#574c40',
                'oruj-green': '#529a4c7a',
                'oruj-bg-red': '#d1433159',
            },
            backgroundImage: {
                'academi-tree': "url('../media/ddl-logo-tree-transparent.png')",
                'academi-tree-portal': "url('../media/ddl-logo-tree-transparent-portal.png')",
                'oruj-logo': "url('../media/oruj-logo.png')",
            },
        },
    },
    plugins: [
        require('flowbite/plugin'),
        require('tailwindcss-rtl'),
    ],
}
