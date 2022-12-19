const server = `http://localhost:8000`

const dlearnService = {
    apiMnistGetMethod, apiMnistPostMethod
}

function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }

async function apiMnistGetMethod(test_num){
    fetch(`${server}/exrc/dlearn/mnist?test_num=${test_num}`)
    .then(handleResponse)
    .then(data=> {
        alert('결과: '+JSON.stringify(data))
    })
}

async function apiMnistPostMethod(test_num){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(test_num)
    }
    fetch(`${server}/exrc/dlearn/mnist`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

export default dlearnService