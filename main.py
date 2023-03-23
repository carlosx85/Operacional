import folium

mapa = folium.Map(location = [-22.3216682098765, -48.7983356481481],
              min_zoom=0, 
              max_zoom=18, 
             zoom_start=18)

folium.Marker(location=[-22.3216682098765, -48.7983356481481],  
              popup = '<i>xxxx</i>', 
              tooltip='<i>Praçãoxxxxxx</i>', 
              icon=folium.Icon(color='black', 
              icon='home', 
              titles='OpenStreetMap',
              prefix='fa',
              min_zoom=0, 
              max_zoom=18, 
              zoom_start=18

              )).add_to(mapa)            
            
mapa

    
