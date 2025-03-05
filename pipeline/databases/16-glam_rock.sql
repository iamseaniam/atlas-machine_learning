-- list all bands with "Glam rock" as main style ranked by longevity
SELECT band_name, 
       (CASE 
            WHEN split IS NULL THEN 2020 - formed 
            ELSE split - formed 
        END) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;