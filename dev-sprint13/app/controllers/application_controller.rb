class ApplicationController < ActionController::Base
  protect_from_forgery
  def index
  	city = request.location.city
  	state= request.location.state

  	if Rails.env.production?
  		@loc = city + ", " + state
  	else
  		@loc = "boston, ma"
  	end
  	loc_pass = String.new(@loc)

  	a = Artist.new
  	@artists = a.search(:artist_location => loc_pass, :sort => 'hotttnesss-desc', :results => '5')

  	p = Playlist.new
  	artist_list = @artists.map{|item| item['name']}
  	@artists.each do |item|
  		item['url'] = a.urls(:name => [item['name']])['official_url']
  		item['img_url'] = a.profile(:name=> [item['name']], :bucket=>['images'])['images'][0]['url']
  	end
  	playlist = p.static(:artist => artist_list)
  	@song_list = ''
  	playlist.each { |x| @song_list = @song_list + x.sub!('spotify:track:', '') + ','}
  	render "index"
  end
  def test
  end
end
