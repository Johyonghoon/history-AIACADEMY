const server = `http://localhost:8000`

const imdbService = {
    apiPostMethod
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

async function apiPostMethod(review){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    }
    const res = await fetch(`${server}/exrc/nlp/imdb`, requestOption)
    .then(handleResponse)
    .then(data => (
        (JSON.stringify(data))
        ))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}

export default imdbService