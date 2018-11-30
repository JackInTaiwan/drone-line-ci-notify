Write your plugin documentation here.

The following parameters are used to configuration the plugin's behavior:

* **url** - The URL to POST the webhook to.

The following is a sample mypluging configuration in your 
.drone.yml file:

```yaml
notify:
  mypluging:
    image: jackintaiwan/mypluging
    url: http://mockbin.org/
```
