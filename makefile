.PHONY: server client test


server:
	cd server && $(MAKE) start

client:
	cd client && $(MAKE) start

test:
	cd test && $(MAKE) test

	
	
	


