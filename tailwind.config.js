/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        'duron-mindful-gray': '#c8bfb6',
        'shade-of-red': '#e2625c',
        'different-shade-of-red': '#e2625cff',
        'shade-of-orange': '#e66019',
        'very-light-shade-of-orange': '#f0eae5',
        'shade-of-green': '#9fbd9a',
      },
      backgroundImage: {
          'academi-tree': "url('../media/ddl-logo-tree-transparent.png')",
      },
    },
  },
  plugins: [],
}
