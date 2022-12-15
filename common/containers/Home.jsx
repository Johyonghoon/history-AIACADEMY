import { Route, Routes } from "react-router-dom"
import { Schedule } from "todos"
import { Counter, Footer, Navigation } from "common"
import { LoginContainer, SignUpContainer } from "auth"
import { StrokeResult } from "exrc"
import IrisResult from "exrc/iris/containers/IrisContainer"


const Home = () => {
    return (<>
    <table style={{ width: "600px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
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
                <Route path="/stroke" element={<strokeContainer/>}></Route>
                <Route path="/iris" element={<IrisResult/>}></Route>
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