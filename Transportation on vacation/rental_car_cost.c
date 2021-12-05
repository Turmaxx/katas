/* d - the days to rent */
const unsigned cost = 40u; 
unsigned rental_car_cost(unsigned d)
{
    if (d >= 3){
        if (d >= 7){
            return (d * cost) - 50u;
        }
        return (d * cost) - 20u;
    }
  
    else if (d >= 1){
        return d * cost;
    }
  
    return 0u;
}