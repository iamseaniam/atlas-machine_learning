-- ranks country origins of bands
SELECT origin, COALESCE(SUM(nb_fans), 0) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;

