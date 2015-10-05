Welcome to the foundation for your Echo Nest application.

You will want to create a `settings.rb` file with the following:

```
API_KEY='yourechonestapikey'
SECRET='somekindofrailsappsecretthatisalphanumericandverylong'
```

Get an Echo Nest API key by visiting the (Echo Nest Developer Site)[https://developer.echonest.com/account/register].

You can generate your SECRET on your own. Look in previous Rails apps that you have made for an example.

Try a few methods out once you have your `settings.rb` file set up...

```
s = Song.new
s.search(:artist => 'green day')
tracks = s.search(:artist => 'green day', :bucket => ['tracks', 'id:spotify-WW']).map do |result|
  hash['tracks'].present? ? hash['tracks'] : nil
end.compact
tracks.map! do |track|
  track[0]['foreign_id'].gsub!('-WW','')
end.uniq!
a = Artist.new
a.search(:name => ['green day'])
p = Playlist.new
p.static(:artist => ['green day']) # you can have multiple artists generate a playlist

```

Additional methods and documentation with arguments can be found in

```
app/models/song.rb
app/models/artist.rb
app/models/playlist.rb
```

That's it! Have fun!