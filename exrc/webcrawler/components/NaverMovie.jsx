import {useState} from 'react'
import webcrawlerService from "../api"
const NaverMovie = () => {
    const [movies, setMovies] = useState([])

    const onClick = e => {
        e.preventDefault()
        webcrawlerService.naverMovie().then(res => {
            const json = JSON.parse(res)
            const arr = json['result']
            for(let i=0; i<arr.length; i++) console.log(arr[i])
            setMovies(arr)
            console.log("arr.length: "+arr.length)
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h2>네이버 영화 크롤러</h2>
    <button onClick={onClick}>네이버 영화 크롤링</button>
    <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
    <table>
        <thead>
            <tr>
            <th>순위</th><th>영화 목록</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>a</td><td>b</td></tr>
            {movies && movies.map((movie, index) =>{
                <tr key={index}><td>{movie.rank}</td><td>{movie.title}</td></tr>
            })}
        </tbody>
    </table>
    </>)
}
export default NaverMovie