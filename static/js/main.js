$(() => {
    if(location.pathname == '/es') {
        $('#en').css({'border' : 'none'})
        $('#es').css({'border-bottom' : '2px solid #ffd1e5'}).fadeIn(500)
        

    } else if(location.pathname == '/en'){
        $('#es').css({'border' : 'none'})
        $('#en').css({'border-bottom' : '2px solid #ffd1e5'}).fadeIn(500)
        
    }
})