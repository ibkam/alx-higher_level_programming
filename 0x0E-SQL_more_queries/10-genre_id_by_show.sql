---  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genres_id
  FROM tv_show_genres
  INNER JOIN tv_shows
  ON tv_shows_id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id;
