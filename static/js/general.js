const response = containerId => {
    let container = document.getElementById(containerId);
    return (r) => (container.innerHTML = r)
}

export {response}