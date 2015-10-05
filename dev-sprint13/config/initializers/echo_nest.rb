if !Rails.env.production?
	require "#{Rails.root}/settings"
	EchoNestApp::Application.config.echo_nest_api_key = API_KEY
else
	EchoNestApp::Application.config.echo_nest_api_key = ENV['API_KEY']
end