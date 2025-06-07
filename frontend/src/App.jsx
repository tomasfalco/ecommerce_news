import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [news, setNews] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/news')
      .then((res) => {
        if (!res.ok) throw new Error('Error al obtener noticias')
        return res.json()
      })
      .then((data) => {
        setNews(data.news)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="container">
      <h1>Novedades de Ecommerce</h1>
      {loading && <p>Cargando noticias...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul className="news-list">
        {news.map((item, idx) => (
          <li key={idx} className="news-item">
            <a href={item.url} target="_blank" rel="noopener noreferrer">
              <h2>{item.title}</h2>
            </a>
            <p dangerouslySetInnerHTML={{ __html: item.summary }} />
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
