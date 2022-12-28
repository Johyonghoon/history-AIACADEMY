import 'common/styles/Home.css'
import { Route, Routes } from "react-router-dom"
import { Schedule } from "todos"
import { Counter, Footer, Navigation } from "common"
import { LoginContainer, SignUpContainer, FashionContainer, IrisContainer, MnistContainer, StrokeContainer, WebCrawlerContainer, SamsungReportContainer, IMDbContainer } from "exrc"


const Home = () => {
    return (<>
    <table style={{ width: "900px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%", height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/signup" element={<SignUpContainer/>}></Route>
                <Route path="/login" element={<LoginContainer/>}></Route>
                <Route path="/stroke" element={<StrokeContainer/>}></Route>
                <Route path="/iris" element={<IrisContainer/>}></Route>
                <Route path="/fashion" element={<FashionContainer/>}></Route>
                <Route path="/mnist" element={<MnistContainer/>}></Route>
                <Route path="/naver-movie" element={<WebCrawlerContainer/>}></Route>
                <Route path="/samsung-report" element={<SamsungReportContainer/>}></Route>
                <Route path="/imdb" element={<IMDbContainer/>}></Route>
            </Routes>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}

export default Home