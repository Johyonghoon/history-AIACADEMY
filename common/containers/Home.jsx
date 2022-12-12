import { Route, Routes } from "react-router-dom"
import { Schedule } from "todos"
import { Counter, Footer, Navigation, Navigation2 } from "common"
import { LoginForm, SignUpForm } from "auth"
import dog from 'images/dog.PNG'
import fashion from 'images/fashion.png'
import { StrokeResult } from "exrc"


const Home = () => {
    const imageSize = {width: 300, height: 300}
    return (<>
    <table style={{ width: "600px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation/>
                    <Navigation2/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr>
            <td>
                <img src={dog} style={imageSize}/>
                <img src={fashion}/>
            </td>
        </tr>
        <tr style={{ width: "20%", height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/count" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/signup" element={<SignUpForm/>}></Route>
                <Route path="/login" element={<LoginForm/>}></Route>
                <Route path="/stroke" element={<StrokeResult/>}></Route>
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