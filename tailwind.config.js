/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        'duron-mindful-gray': '#c8bfb6',
        'shade-of-red': '#aa6562',
        'shade-of-orange': '#e66019',
      },
    },
  },
  plugins: [],
}
