              //var location = { lat: parseInt(latitude), lng: parseInt(longitude) };
              // var new_loc = {lat: 21.1458,lng:79.0882};
              var iconBase = 'https://www.flaticon.com/free-icon/';
              var marker = new google.maps.Marker({
                  position: location,
                 map: map,
                 icon: iconBase + 'car.png'
              
             });
              var marker = new google.maps.Marker({
                position: new_loc,
                map: map,
                icon: iconBase + 'car.png'
                
              });
           